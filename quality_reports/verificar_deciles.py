"""Coteja tabla 1 del PDF de Núñez con JSON, CSV y coordenadas de la gráfica.

Uso: python verificar_deciles.py /ruta/Bienestar.pdf
No replica la microsimulación ni certifica sus supuestos.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv, hashlib, json, re, sys
import pypdfium2 as pdf

ROOT = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1])
doc = pdf.PdfDocument(str(source))
text = re.sub(r'\s+', ' ', doc[7].get_textpage().get_text_range()).replace('−', '-')
pattern = r'(?<![\d.,])([1-9]|10)\s+' + r'\s+'.join([r'(-?\d+,\d+)'] * 9)
rows = {int(m[0]): [Decimal(v.replace(',', '.')) for v in m[1:]] for m in re.findall(pattern, text)}
assert set(rows) == set(range(1, 11)), rows
data = json.loads((ROOT/'data/incidencia_nunez.json').read_text(encoding='utf-8'))
csvrows = list(csv.DictReader((ROOT/'data/incidencia_nunez.csv').open(encoding='utf-8')))
tex = (ROOT/'data/grafico_deciles.tex').read_text(encoding='utf-8')
plots = re.findall(r'coordinates \{([^}]+)\}', tex)
assert len(plots) == 2
checks = []
for scenario, column, plot, csvcol in zip(['plena','restringida'], [4,7], plots, ['plena_pct_recursos','restringida_pct_recursos']):
    points = {int(i): Decimal(v) for i,v in re.findall(r'\((\d+),(-?[\d.]+)\)', plot)}
    for row, csvrow in zip(data['datos'], csvrows):
        i = row['decil']
        expected = rows[i][column]
        values = {'json': Decimal(row[scenario]), 'csv': Decimal(csvrow[csvcol]), 'grafica': points[i]}
        for kind, actual in values.items():
            target = expected.quantize(Decimal('.1'), rounding=ROUND_HALF_UP) if kind == 'grafica' else expected
            checks.append({'decil':i,'escenario':scenario,'canal':kind,'fuente':str(expected),'esperado':str(target),'salida':str(actual),'resultado':'PASS' if actual == target else 'FAIL'})
assert hashlib.sha256(source.read_bytes()).hexdigest() == data['sha256_documento']
report = {'fuente':data['titulo'],'autor':data['autor'],'version':data['version'],'pagina':8,'sha256':data['sha256_documento'],'alcance':'Transcripción de tabla 1, CSV y redondeo de los 20 puntos de la gráfica. No certifica la microsimulación ni la incidencia de toda la reforma.','PASS':sum(c['resultado']=='PASS' for c in checks),'FAIL':sum(c['resultado']=='FAIL' for c in checks),'checks':checks}
(ROOT/'quality_reports/cotejo_deciles.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False,indent=2))
sys.exit(bool(report['FAIL']))
