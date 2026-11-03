"""Regenera equivalencias en COP y concilia categorías de la tabla 14 oficial.

Python 3, biblioteca estándar. No estima respuestas de comportamiento ni certifica
el ahorro del proyecto desde microdatos. Tasas y umbrales: PL477/2026C radicado.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv, json

ROOT = Path(__file__).resolve().parents[1]
UVT = Decimal(52374)
SM = Decimal(1750905)
VALUES = {
    'UVTpesos': UVT, 'SMpesos': SM,
    'PisoAnual': 720*UVT, 'PisoMensual': 720*UVT/12,
    'TechoAnual': 1090*UVT, 'TechoMensual': 1090*UVT/12,
    'EjemploBase': 900*UVT,
    'EjemploImpuesto': (900-720)*Decimal('.09')*UVT,
    'EjemploMes': (900-720)*Decimal('.09')*UVT/12,
    'Dependiente': 72*UVT,
    'ExentaAntes': 790*UVT, 'ExentaDespues': 630*UVT,
    'TopeAntes': 1340*UVT, 'TopeDespues': 1180*UVT,
    'DevolucionTope': Decimal('5.5')*UVT,
    'SalarioEjemplo': 4*SM,
    'SaludAntes': Decimal('.04')*4*SM,
    'SaludDespues': Decimal('.055')*4*SM,
    'SaludDiferencia': Decimal('.015')*4*SM,
    'EmpresaSalud': Decimal('.085')*4*SM,
    'EmpresaParafiscal': Decimal('.05')*4*SM,
    'EmpresaTotal': Decimal('.135')*4*SM,
    'ControversiaUmbral': 2000000*UVT,
}
def pesos(n):
    return f'{n.quantize(Decimal(1), rounding=ROUND_HALF_UP):,.0f}'.replace(',', '.')

def main():
    with (ROOT/'data/conversiones.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['concepto','COP_sin_redondear','COP_redondeado'])
        for k,v in VALUES.items():w.writerow([k,str(v),pesos(v)])
    (ROOT/'data/conversiones.tex').write_text('\n'.join('\\newcommand{\\'+k+'}{'+pesos(v)+'}' for k,v in VALUES.items())+'\n',encoding='utf-8')
    original=json.loads((ROOT/'data/tabla14_fuente.json').read_text(encoding='utf-8'))
    config=json.loads((ROOT/'data/clasificacion_medidas.json').read_text(encoding='utf-8'))
    excluded={r['concepto'] for r in original['filas'] if r['concepto'].startswith(('I.','II.','III.','IV.','VI.'))}
    excluded.update(['Efecto de la Ley de Rescate en el Balance Primario','Otras medidas de ajuste fiscal','Efecto Total de la Estrategia de Ajuste Fiscal','Enajenaciones'])
    used=[k for r in config['filas'] for k in r['filas_fuente']]
    assert len(used)==len(set(used)), 'Una fila de fuente se cuenta más de una vez'
    assert set(used)=={r['concepto'] for r in original['filas']}-excluded, 'Faltan medidas o entran filas externas a la ley'
    fiscal={}
    detailed=[]
    for year in ['2027','2028','2029','2030']:
        raw={r['concepto']:Decimal(r[year]) for r in original['filas']}
        vals={r['id']:sum((raw[k] for k in r['filas_fuente']),Decimal(0)) for r in config['filas']}
        total=raw['Efecto de la Ley de Rescate en el Balance Primario']
        difference=total-sum(vals.values())
        vals['diferencia_suma']=difference
        vals['total_ley']=total
        fiscal[year]={'medidas':{k:f'{v:.2f}' for k,v in vals.items()},'resumen':{
          'recortes_brutos':f"{sum(vals[k] for k in ['eficiencia_gasto','personal','ops']):.2f}",
          'mayor_gasto_sgp':f"{-vals['sgp']:.2f}",
          'menor_gasto_neto':f"{sum(vals[r['id']] for r in config['filas'] if r['grupo']=='gasto'):.2f}",
          'cotizaciones':f"{sum(vals[r['id']] for r in config['filas'] if r['grupo']=='cotizaciones'):.2f}",
          'impuestos_y_gestion_netos':f"{sum(vals[r['id']] for r in config['filas'] if r['grupo']=='impuestos'):.2f}",
          'reasignacion_cajas':f"{vals['ccf']:.2f}",'efectos_macro':f"{vals['efectos_macro']:.2f}",
          'diferencia_suma':f'{difference:.2f}','total_ley':f'{total:.2f}'}}
        for r in config['filas']:
            detailed.append([year,r['id'],r['etiqueta'],r['grupo'],f"{vals[r['id']]:.2f}",' | '.join(r['filas_fuente'])])
        detailed.extend([[year,'diferencia_suma','Diferencia frente al total publicado','conciliacion',f'{difference:.2f}','Total publicado menos suma de componentes redondeados'],[year,'total_ley','Total del proyecto','total',f'{total:.2f}','Efecto de la Ley de Rescate en el Balance Primario']])
        assert sum(vals[r['id']] for r in config['filas'])+difference==total
    with (ROOT/'data/ajuste_oficial.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['vigencia','id','medida','grupo','impacto_pp_PIB','filas_fuente']);w.writerows(detailed)
    doc={'fuente':config['fuente'],'unidad':config['unidad'],'criterio':config['criterio'],
         'naturaleza':'Estimaciones oficiales reclasificadas por mecanismo. La diferencia de suma se muestra explícitamente y no se trata como medida fiscal.',
         'limites':config['limites'],'datos':fiscal}
    (ROOT/'data/ajuste_oficial.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    def display(value):
        rounded=Decimal(value).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP)
        if rounded==0:rounded=abs(rounded)
        return f'{rounded:.1f}'.replace('.',',')
    def number(id,year):return display(fiscal[year]['medidas'][id])
    def summary_number(id,year):return display(fiscal[year]['resumen'][id])
    colors={'gasto':('G','rust'),'cotizaciones':('I','teal'),'impuestos':('I','teal'),'efectos_macro':('I','teal'),'reasignacion':('R','muted')}
    def line(label,id,summary=False,bold=False,group=None):
        get=summary_number if summary else number
        cells=[label,get(id,'2027'),get(id,'2030')]
        if bold:cells=[r'\textbf{'+c+'}' for c in cells]
        if group:
            code,color=colors[group]
            cells=[r'\textcolor{'+color+'}{'+code+'}',r'\textcolor{'+color+'}{'+cells[0]+'}',*cells[1:]]
        else:cells=['',*cells]
        return ' & '.join(cells)+r'\\'
    # Orden por impacto de 2030 antes del redondeo. Los efectos negativos quedan al final.
    mainrows=[dict(r,summary=False) for r in config['filas']]
    def sortvalue(r):
        values=fiscal['2030']['resumen'] if r['summary'] else fiscal['2030']['medidas']
        return Decimal(values[r['id']])
    mainrows.sort(key=sortvalue,reverse=True)
    latex=[line(r['etiqueta'],r['id'],summary=r['summary'],group=r['grupo']) for r in mainrows]
    latex.extend([r'\midrule',line('Total del proyecto','total_ley',bold=True),r'\bottomrule'])
    (ROOT/'data/cuadro_ajuste.tex').write_text('\n'.join(latex)+'\n',encoding='utf-8')
    for threshold in [8140000,5530000,2580000]:print('RUGE',threshold,'UVT =',threshold*UVT,'COP')
    print('Conversiones regeneradas y sumas conciliadas para 2027-2030.')

if __name__=='__main__':main()
