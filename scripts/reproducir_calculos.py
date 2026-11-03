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
    fiscal={}
    for year in ['2027','2028','2029','2030']:
        rows={r['concepto']:Decimal(r[year]) for r in original['filas']}
        spending=sum(rows[k] for k in [
            'Mejoramiento en la eficiencia del gasto público (RDE, Fondos Especiales, Resto de Transferencias)',
            'Variación de Gastos de Personal - Facultades Extraordinarias',
            'Reducción en contratación por OPS - Austeridad en la contratación estatal',
            'Mayor Gasto - Incremento en SGP'])
        social=sum(rows[k] for k in [
            'Exoneración de aportes al empleador (Sena, ICBF, Salud)',
            'Cotizaciones a salud de empleados independientes y regimenes especiales',
            'Redirigir un punto de cotización de CCF a salud',
            'Impuesto al consumo de tabaco y bebidas alcohólicas para salud'])
        total=rows['Efecto de la Ley de Rescate en el Balance Primario']
        fiscal[year]={'gasto_neto':str(spending),'financiacion_social':str(social),
                      'otros_efectos_netos':str(total-spending-social),'total_ley':str(total)}
    with (ROOT/'data/ajuste_oficial.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['vigencia','gasto_neto','financiacion_social','otros_efectos_netos','total_ley'])
        for y,r in fiscal.items():
            assert sum(Decimal(r[k]) for k in ['gasto_neto','financiacion_social','otros_efectos_netos'])==Decimal(r['total_ley'])
            w.writerow([y,*r.values()])
    doc={'fuente':'Exposición PL477/2026C, tabla14, página204',
         'unidad':'puntos del PIB',
         'naturaleza':'Estimaciones oficiales. Otros efectos netos es residuo contable e incluye retroalimentación macroeconómica. No es reproducción independiente desde microdatos.',
         'datos':fiscal}
    (ROOT/'data/ajuste_oficial.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for threshold in [8140000,5530000,2580000]:print('RUGE',threshold,'UVT =',threshold*UVT,'COP')
    print('Conversiones regeneradas y sumas conciliadas para 2027-2030.')

if __name__=='__main__':main()
