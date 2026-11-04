# La Ley de Rescate Económico

Presentación en Beamer sobre una selección de medidas del Proyecto de Ley 477/2026C. Oliver Pardo. Corte: 3 de noviembre de 2026.

## Abrir y compilar

Abrir `main.tex` en Overleaf, con pdfLaTeX, XeLaTeX o Tectonic. El repositorio conserva las rutas relativas y no depende de fuentes instaladas localmente.

```sh
tectonic main.tex
```

El PDF se genera como `main.pdf`. Las primeras 21 diapositivas constituyen la presentación. Al final hay cuatro anexos.

## Unidades y fuentes

Las conversiones usan UVT 2026 de $52.374 y salario mínimo 2026 de $1.750.905. Los pesos son equivalencias ilustrativas. Las unidades de las vigencias de aplicación serán diferentes. Los equivalentes mensuales de renta dividen la base o impuesto anual entre 12 y no equivalen a salario bruto o retención mensual.

Las cifras fiscales son estimaciones de Hacienda, tabla 14 de la exposición de motivos, página 204. No son ahorros certificados desde microdatos. La diapositiva 4 distingue gasto neto, cotizaciones, impuestos netos, reasignación de las cajas y efectos macroeconómicos. `data/clasificacion_medidas.json` identifica cada fila fuente. `data/ajuste_oficial.csv` y `.json` reconstruyen 2027–2030 sin duplicar medidas. Los cuadros y el gráfico fiscal muestran una sola cifra decimal. Los cálculos conservan la precisión de la fuente y los totales se redondean después de sumar. Las diferencias pequeñas de conciliación se conservan solo en los archivos de cálculo.

Las referencias aparecen al pie de cada diapositiva. [Proyecto oficial](https://www.camara.gov.co/ley-rescate-economico/).

## Cálculos

`scripts/reproducir_calculos.py` regenera `data/conversiones.tex` y los CSV. Solo requiere Python 3. Los umbrales RUGE son inversión, no ingresos. Los 2 millones de UVT del artículo 95 son el valor de la obligación en discusión, no un beneficio fiscal de esa cuantía.

El repositorio incluye la figura compartida usada en la apertura. Los documentos privados de trabajo y sus PDF completos permanecen en el archivo local. Las fuentes públicas se enlazan.

## Revisión

[Meta Skill Review Oliver](quality_reports/meta_skill_review.md): lectura y revisión independiente de la versión inicial. La última desagregación se cotejó contra las 20 filas de medidas de la tabla 14, con comprobaciones de fuentes, sumas y redondeo aprobadas. El historial distingue cada versión.

Para repetir el cotejo, descargar el PDF oficial de 334 páginas y ejecutar:

```sh
python quality_reports/auditar_cifras.py nueva_revision /ruta/proyecto_oficial.pdf
```

El historial de comprobaciones se conserva en `quality_reports/replication-log.md`. Las estimaciones fiscales siguen siendo las oficiales, no una auditoría independiente del ajuste neto.

## Formato académico

El formato reproduce `presentacion_javeriana.tex` del paper *Beyond Formality* (Pardo y Orozco): Beamer de 11 puntos, fondo blanco, texto negro, títulos azules y pie institucional. El logo procede de esa misma presentación. Se conservan las referencias visibles para consultar las medidas del proyecto. La versión actual incluye 21 diapositivas y cuatro anexos.

El cuadro 4 reúne todas las medidas presentadas en un único cuadro con columnas para 2027 y 2030, ordenado por magnitud del efecto fiscal en 2030 y con una cifra decimal. Azul (I): ingresos, rojo oscuro (G): gasto y gris (R): reasignación. El signo indica si la medida mejora o reduce el ajuste. Las cotizaciones de empleadores y personas figuran por separado.

La secuencia de bloques sigue la magnitud absoluta del efecto fiscal en 2030, incluido el costo de las rebajas. IVA va primero. Personal y OPS se consideran un bloque. La normalización se presenta como transitoria y RUGE y artículo 95 como beneficios de costo no cuantificado. `data/orden_presentacion.json` documenta el orden y sus fuentes.

## IVA y distribución por deciles

La tabla de IVA compara una selección de bienes en el régimen general de 2026 con el proyecto desde 2028. `data/iva_antes_despues.json` identifica partidas y artículos. Excluido y exento al 0% no son equivalentes.

La gráfica por deciles da crédito a Jairo Núñez Méndez, *Bienestar social y Ley de Rescate Económico*, borrador para discusión del 30 de octubre de 2026, tabla 1, p. 8. `data/incidencia_nunez.csv` conserva las cifras publicadas con dos decimales y la gráfica las muestra con uno. Compara devolución plena y restringida a compras con factura. Son deciles de gasto per cápita, no de ingreso. La simulación calibrada cubre medidas sobre hogares y no toda la reforma. El anexo precisa sus supuestos. No se reproducen los microdatos ni se publica el documento privado compartido en Mesa Fiscal.

## Referencias al articulado

Las diapositivas de medidas muestran bajo el título los artículos pertinentes del proyecto, con enlaces al inicio de cada disposición en el PDF oficial. La tabla de IVA identifica además el artículo por grupo de bienes. El balance agregado remite a la tabla 14 de la exposición de motivos. Las gráficas de incidencia identifican las medidas simuladas y conservan el crédito a Jairo Núñez. La correspondencia se registra en `data/referencias_articulos.json`. Se cotejaron 45 referencias con sus destinos y las anotaciones del PDF.

## Requisitos y garantías de EfectIVA

Las diapositivas 6 y 7 distinguen elegibilidad, identificación de compras, canales de pago, porcentajes devueltos, topes y mínimos. Artículos 38–40 del texto radicado. Existe un mínimo para pobreza extrema independiente del IVA registrado, con cuantía definida por Hacienda. El transitorio 3 del artículo 40 garantiza que la suma de devoluciones del hogar al migrar desde la compensación vigente no sea inferior a la compensación previa. No se exige tarjeta para toda compra ni cuenta como requisito universal para recibir el pago.

## Contrafactual de apertura

La diapositiva 2 presenta la figura compartida de Núñez que compara reforma con EfectIVA plena, reforma con devolución limitada a factura y crisis sin reforma, hacia2030. Se conserva la imagen original y su hash en `data/crisis_nunez.json`. El encuadre mantiene barras, ejes y leyenda. El choque macroeconómico procede de Hacienda y el supuesto de caída uniforme en los deciles4–10 de Núñez. El documento metodológico no tabula el valor exacto de esa serie, por lo que no se digitalizaron ni inventaron cifras para reconstruirla. La comparación es condicional a la crisis. No estima su probabilidad ni incluye otro paquete de ajuste.

## Tabla de ingreso y fuente común de Núñez

El primer anexo incorpora los cortes de ingreso disponible de la tabla facilitada por Oliver. No se confunden con los deciles de gasto de las gráficas. Los valores redondeados se conservan tal como se facilitaron, sin recalcular multiplicaciones. JSON, CSV y TeX guardan la transcripción. No se trata de cifras corrientes de DANE para 2026 ni de umbrales legales de EfectIVA. La fuente común del material se identifica como Jairo Núñez Méndez (2026), *Bienestar social y Ley de Rescate Económico*, documento compartido por Daniel Wills. El PDF metodológico conservado tiene 15 páginas y no incluye esta tabla complementaria. No se replicaron sus microdatos.
