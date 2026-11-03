from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timezone
import json,re,csv,sys,platform,hashlib,subprocess
import pypdfium2 as pdf

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'quality_reports';OUT.mkdir(exist_ok=True)
SOURCEPDF=Path(sys.argv[2]) if len(sys.argv)>2 else ROOT.parent/'seguimiento_ley_rescate/fuentes/pl477_camara_original_20261029.pdf'
RUN=sys.argv[1] if len(sys.argv)>1 else 'inicial'
tex=(ROOT/'main.tex').read_text(encoding='utf-8')
doc=pdf.PdfDocument(ROOT/'main.pdf')
pages=[re.sub(r'\s+',' ',doc[i].get_textpage().get_text_range()) for i in range(len(doc))]
claims=[]
def check(id,slide,reported,expected,method,tolerance=Decimal(0),shown=None,kind='calculo'):
    reported=Decimal(str(reported));expected=Decimal(str(expected));diff=abs(reported-expected)
    present=True if shown is None else shown in pages[slide-1]
    claims.append({'id':id,'slide':slide,'reported':str(reported),'computed':str(expected),
                   'difference':str(diff),'tolerance':str(tolerance),'pdf_display_found':present,
                   'method':method,'kind':kind,'status':'PASS' if diff<=tolerance and present else 'FAIL'})

u=Decimal(52374);sm=Decimal(1750905)
def roundpeso(x):return x.quantize(Decimal(1),rounding=ROUND_HALF_UP)
defs={k:v for k,v in re.findall(r'\\newcommand\{\\(\w+)\}\{([0-9.]+)\}',(ROOT/'data/conversiones.tex').read_text(encoding='utf-8'))}
source_slide=next(i+1 for i,t in enumerate(pages) if 'Anexo. Convenciones y fuentes' in t)
formulas={
 'UVTpesos':(source_slide,u,'UVT2026 según resolución238/2025'),
 'SMpesos':(source_slide,sm,'SMLMV2026 según decreto159/2026'),
 'PisoAnual':(6,720*u,'720*52374'), 'PisoMensual':(6,720*u/12,'720*52374/12'),
 'TechoAnual':(6,1090*u,'1090*52374'),'TechoMensual':(6,1090*u/12,'1090*52374/12'),
 'EjemploImpuesto':(6,(900-720)*Decimal('.09')*u,'(900-720)*0.09*52374'),
 'EjemploMes':(6,(900-720)*Decimal('.09')*u/12,'(900-720)*0.09*52374/12'),
 'ExentaAntes':(7,790*u,'790*52374'),'ExentaDespues':(7,630*u,'630*52374'),
 'Dependiente':(7,72*u,'72*52374'),'SalarioEjemplo':(8,4*sm,'4*1750905'),
 'SaludAntes':(8,4*sm*Decimal('.04'),'4*1750905*0.04'),
 'SaludDespues':(8,4*sm*Decimal('.055'),'4*1750905*0.055'),
 'SaludDiferencia':(8,4*sm*Decimal('.015'),'4*1750905*(0.055-0.04), solo aporte a salud'),
 'EmpresaTotal':(9,4*sm*Decimal('.135'),'4*1750905*(0.085+0.02+0.03)'),
 'DevolucionTope':(13,Decimal('5.5')*u,'5.5*52374')}
for name,(slide,value,method) in formulas.items():
    shown=defs[name];check('COP_'+name,slide,shown.replace('.',''),roundpeso(value),method,shown=shown)

# La fuente es el PDF público de334páginas, no la transcripción como oráculo.
original=pdf.PdfDocument(SOURCEPDF)
t14=re.sub(r'\s+',' ',original[203].get_textpage().get_text_range())
table=json.loads((ROOT/'data/tabla14_fuente.json').read_text(encoding='utf-8'))
direct={}
for row in table['filas']:
    m=re.search(re.escape(row['concepto'])+r'\s+(-?[0-9,]+)%\s+(-?[0-9,]+)%\s+(-?[0-9,]+)%\s+(-?[0-9,]+)%',t14)
    if not m:raise ValueError('Fila no localizada en página204: '+row['concepto'])
    direct[row['concepto']]=[Decimal(v.replace(',','.')) for v in m.groups()]
totals=direct['Efecto de la Ley de Rescate en el Balance Primario']
plot=re.search(r'\\addplot\[fill=teal,draw=none\] coordinates \{([^}]+)\}',tex).group(1)
for i,(year,value) in enumerate(re.findall(r'\((\d{4}),([0-9.]+)\)',plot)):
    check('GRAFICO_'+year,2,value,totals[i],'PDF oficial p204, fila efecto de la ley',shown=value)

summary=json.loads((ROOT/'data/ajuste_oficial.json').read_text(encoding='utf-8'))['datos']
config=json.loads((ROOT/'data/clasificacion_medidas.json').read_text(encoding='utf-8'))
used=[k for r in config['filas'] for k in r['filas_fuente']]
excluded={k for k in direct if k.startswith(('I.','II.','III.','IV.','VI.'))}
excluded.update(['Efecto de la Ley de Rescate en el Balance Primario','Otras medidas de ajuste fiscal','Efecto Total de la Estrategia de Ajuste Fiscal','Enajenaciones'])
check('FILAS_SIN_DOBLE_CONTEO',3,len(used),len(set(used)),'Cada medida fuente se utiliza una sola vez')
check('COBERTURA_DE_MEDIDAS',3,len(set(used)&(set(direct)-excluded)),len(set(direct)-excluded),'Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional')
assert set(used)==set(direct)-excluded
expected={}
for i,year in enumerate(['2027','2028','2029','2030']):
    values={r['id']:sum((direct[k][i] for k in r['filas_fuente']),Decimal(0)) for r in config['filas']}
    values['diferencia_suma']=totals[i]-sum(values.values())
    values['total_ley']=totals[i]
    expected[year]=values
    for id,v in values.items():
        check('SALIDA_'+id+'_'+year,3,summary[year]['medidas'][id],v,'Filas identificadas de la página 204 del PDF oficial')
    check('CONCILIACION_'+year,3,sum(Decimal(v) for k,v in summary[year]['medidas'].items() if k!='total_ley'),totals[i],'Suma de todas las medidas y diferencia publicada, sin duplicación')

def check_tex_row(label,id,slide,filename,values):
    rawtex=(ROOT/'data'/filename).read_text(encoding='utf-8')
    pattern=r'^\s*(?:\\quad )?(?:\\textbf\{)?'+re.escape(label)+r'\}?\s*&\s*(?:\\textbf\{)?(-?[0-9,]+)\}?\s*&\s*(?:\\textbf\{)?(-?[0-9,]+)'
    match=re.search(pattern,rawtex,re.M)
    if not match:raise ValueError('Fila generada no localizada: '+label)
    for year,raw in zip(['2027','2030'],match.groups()):
        check('FISCAL_'+id+'_'+year,slide,raw.replace(',','.'),values[year],'TeX y PDF de diapositivas contra sumas del PDF oficial p204',shown=raw)
for row in config['filas']:
    slide=3 if row['grupo'] in ['gasto','reasignacion','efectos_macro'] else 4
    filename='cuadro_ajuste.tex' if slide==3 else 'cuadro_ingresos.tex'
    check_tex_row(row['etiqueta'] if row['id']!='ccf' else 'Reasignación de las cajas a salud',row['id'],slide,filename,{y:expected[y][row['id']] for y in expected})
for id,label in [('diferencia_suma','Diferencia frente al total publicado'),('total_ley','Total del proyecto')]:
    check_tex_row(label,id,3,'cuadro_ajuste.tex',{y:expected[y][id] for y in expected})
for key,label,group in [('menor_gasto_neto','Menor gasto neto','gasto'),('cotizaciones','Mayores cotizaciones','cotizaciones'),('impuestos_y_gestion_netos','Impuestos y gestión, netos de rebajas','impuestos')]:
    vals={y:sum(expected[y][r['id']] for r in config['filas'] if r['grupo']==group) for y in expected}
    check_tex_row(label,key,3,'cuadro_ajuste.tex',vals)
    for y,v in vals.items():check('RESUMEN_'+key+'_'+y,3,summary[y]['resumen'][key],v,'Agrupación por mecanismo desde el PDF oficial')
values={y:sum(expected[y][r['id']] for r in config['filas'] if r['grupo'] in ['cotizaciones','impuestos']) for y in expected}
check_tex_row('Mayores ingresos netos por estas medidas','ingresos_medidas',4,'cuadro_ingresos.tex',values)

for uvts,value in [(8140000,'426.3'),(5530000,'289.6'),(2580000,'135.1')]:
    expected=(Decimal(uvts)*u/Decimal(10**9)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP)
    check('RUGE_'+str(uvts),16,value,expected,f'{uvts}*52374/1e9, redondeado a0.1',shown=value.replace('.',','))
check('UMBRAL95',18,104748,2000000*u/1000000,'2e6*52374/1e6; millones COP',shown='104.748')
for id,slide,rep,calc,method,shown in [
 ('PRECIO_IVA5',12,105000,100000*Decimal('1.05'),'100000*1.05','105.000'),
 ('PRECIO_IVA19',12,119000,100000*Decimal('1.19'),'100000*1.19','119.000'),
 ('VAR_PRECIO_IVA',12,'13.3',(Decimal(119)/105-1)*100,'(119/105-1)*100','13,3'),
 ('RENTA_EMPRESA35',15,350,1000*Decimal('.35'),'1000*0.35, millonesCOP','350'),
 ('RENTA_EMPRESA31',15,310,1000*Decimal('.31'),'1000*0.31, millonesCOP','310'),
 ('NORMALIZACION15',17,150,1000*Decimal('.15'),'1000*0.15, millonesCOP','150')]:
    check(id,slide,rep,calc,method,Decimal('.05') if id=='VAR_PRECIO_IVA' else Decimal(0),shown=shown)

# Un diagrama cuantitativo debe respetar también su proporción.
ma=re.search(r'fill\[navy!70\] \(2\.1,0\) rectangle \(([0-9.]+),1\.15\)',tex)
actual=Decimal(2)/(Decimal(2)+Decimal(ma.group(1))-Decimal('2.1'))*100
check('DIAGRAMA_CAJAS',11,actual,25,'Anchos de segmentos TikZ,1de4puntos',Decimal('.1'))

report={'skill':'audit-reproducibility-santanna, aplicación acotada a cifras de diapositivas',
 'run':RUN,'date_utc':datetime.now(timezone.utc).isoformat(),'baseline_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
 'pdf_sha256':hashlib.sha256((ROOT/'main.pdf').read_bytes()).hexdigest(),
 'source_pdf_sha256':hashlib.sha256((SOURCEPDF).read_bytes()).hexdigest(),
 'environment':{'python':platform.python_version(),'platform':platform.platform()},
 'scope':'Conversiones monetarias, ejemplos aislados, gráfico fiscal, cuadros de gasto e ingresos, cobertura de medidas, conciliación y proporción visual. Comparación horizontal TeX/PDF/JSON para los campos declarados. Las tasas legales se cotejan en la revisión sustantiva.',
 'limits':'No certifica microdatos, base fiscal, elegibilidad de empresas ni ahorro independiente. No compara con la columna entregada, otro artefacto con alcance distinto. Fechas, identificadores de norma y números de página no son estimaciones.',
 'claims':claims,'pass':sum(c['status']=='PASS' for c in claims),'fail':sum(c['status']=='FAIL' for c in claims)}
(OUT/f'reproducibility_claims_slides_{RUN}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
header=['# Auditoría numérica de las diapositivas','',f"Corrida {RUN}. {report['pass']} PASS, {report['fail']} FAIL.",'',report['scope'],'',report['limits'],'','| Afirmación | Diap. | Mostrado | Recalculado | Resultado |','|---|---:|---:|---:|---|']
header += [f"| {c['id']} | {c['slide']} | {c['reported']} | {c['computed']} | {c['status']} |" for c in claims]
(OUT/f'reproducibility_audit_slides_{RUN}.md').write_text('\n'.join(header)+'\n',encoding='utf-8')
log=OUT/'replication-log.md'
with log.open('a',encoding='utf-8') as f:
    if log.stat().st_size==0:f.write('# Registro de comprobaciones numéricas\n\nHistorial acumulativo. Las correcciones se registran como nuevas corridas.\n\n')
    f.write(f"## {report['date_utc']} — {RUN}, base {report['baseline_commit']}\n\n{report['pass']} PASS, {report['fail']} FAIL.\n\n| Afirmación | Mostrado | Recalculado | Método | Resultado |\n|---|---:|---:|---|---|\n")
    for c in claims:f.write(f"| {c['id']} | {c['reported']} | {c['computed']} | {c['method']} | {c['status']} |\n")
print(json.dumps({'pass':report['pass'],'fail':report['fail'],'failed':[c for c in claims if c['status']=='FAIL']},ensure_ascii=False,indent=2))

sys.exit(1 if report['fail'] else 0)
