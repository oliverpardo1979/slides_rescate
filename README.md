# La Ley de Rescate Económico

Presentación en Beamer sobre una selección de medidas del Proyecto de Ley 477/2026C. Oliver Pardo. Corte: 3 de noviembre de 2026.

## Abrir y compilar

Abrir `main.tex` en Overleaf, con pdfLaTeX, XeLaTeX o Tectonic. El repositorio conserva las rutas relativas y no depende de fuentes instaladas localmente.

```sh
tectonic main.tex
```

El PDF se genera como `main.pdf`. Las primeras 19 diapositivas constituyen la presentación. Al final hay dos anexos.

## Unidades y fuentes

Las conversiones usan UVT 2026 de $52.374 y salario mínimo 2026 de $1.750.905. Los pesos son equivalencias ilustrativas. Las unidades de las vigencias de aplicación serán diferentes. Los equivalentes mensuales de renta dividen la base o impuesto anual entre 12 y no equivalen a salario bruto o retención mensual.

Las cifras fiscales son estimaciones de Hacienda, tabla 14 de la exposición de motivos, página 204. No son ahorros certificados desde microdatos. Las diapositivas 3 y 4 distinguen gasto neto, cotizaciones, impuestos netos, reasignación de las cajas y efectos macroeconómicos. `data/clasificacion_medidas.json` identifica cada fila fuente. `data/ajuste_oficial.csv` y `.json` reconstruyen 2027–2030 sin duplicar medidas. Las diferencias entre los componentes redondeados y el total publicado permanecen visibles: 0,00, −0,02, 0,00 y −0,01 puntos del PIB, respectivamente. No se presenta esa diferencia como una medida fiscal.

Las referencias aparecen al pie de cada diapositiva. [Proyecto oficial](https://www.camara.gov.co/ley-rescate-economico/).

## Cálculos

`scripts/reproducir_calculos.py` regenera `data/conversiones.tex` y los CSV. Solo requiere Python 3. Los umbrales RUGE son inversión, no ingresos. Los 2 millones de UVT del artículo 95 son el valor de la obligación en discusión, no un beneficio fiscal de esa cuantía.

El repositorio no incluye los documentos privados de trabajo ni los originales proporcionados por Oliver. Las fuentes públicas se enlazan.

## Revisión

[Meta Skill Review Oliver](quality_reports/meta_skill_review.md): lectura y revisión independiente de la versión inicial. La última desagregación se cotejó contra las 20 filas de medidas de la tabla 14, con 154 comprobaciones aprobadas. El historial distingue cada versión.

Para repetir el cotejo, descargar el PDF oficial de 334 páginas y ejecutar:

```sh
python quality_reports/auditar_cifras.py nueva_revision /ruta/proyecto_oficial.pdf
```

El historial de comprobaciones se conserva en `quality_reports/replication-log.md`. Las estimaciones fiscales siguen siendo las oficiales, no una auditoría independiente del ajuste neto.

## Formato académico

El formato reproduce `presentacion_javeriana.tex` del paper *Beyond Formality* (Pardo y Orozco): Beamer de 11 puntos, fondo blanco, texto negro, títulos azules y pie institucional. El logo procede de esa misma presentación. Se conservan las referencias visibles para consultar las medidas del proyecto. La versión actual incluye 19 diapositivas y dos anexos.
