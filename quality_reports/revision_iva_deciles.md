# IVA y efecto por deciles

Revisión del 3 de noviembre de 2026. Cambios en las diapositivas 4, 18 y 21. Las demás conservan el contenido y orden acordados con Oliver.

## Cotejo del IVA

Se compararon diez filas de ejemplos con el Estatuto Tributario compilado por DIAN, consultado el 3 de noviembre de 2026, y con el original de Cámara del proyecto 477/2026C. `data/iva_antes_despues.json` identifica las partidas.

- Papa, yuca, pan horneado y arepa de maíz continúan excluidos por el artículo 42.
- Banano, manzana, tomate y cebolla frescos salen de la lista de excluidos del artículo 424 y quedan en la tarifa general de 19%.
- Carne de res, pollo, leche y huevos conservan la exención del artículo 477, modificado por el artículo 46 del proyecto.
- Queso fresco, actualmente exento en la partida 04.06.10.00.00, no figura en los nuevos artículos 424 ni 477 y pasa al 19%.
- Los medicamentos de las partidas 30.03 y 30.04 conservan la exención.
- Café tostado y pastas sin cocer ni rellenar pasan del 5% al 19% por la derogatoria del artículo 468-1 desde 2028.
- Ropa corriente permanece en el régimen general de 19%.

Es una selección del régimen general, sin excepciones territoriales. No se confundió exclusión con exención ni se afirmó que todo pase al 19%. Confianza High sobre estos ejemplos del texto radicado, sujeto a cambios en el trámite.

Fuentes: [DIAN, Estatuto Tributario](https://normograma.dian.gov.co/dian/compilacion/docs/estatuto_tributario.htm), arts. 424, 468, 468-1 y 477. [Proyecto oficial](https://www.camara.gov.co/ley-rescate-economico/), arts. 42 y 46, pp. 248–258, y art. 106, p. 333.

## Incidencia por deciles

Se leyó el documento completo de Jairo Núñez Méndez, *Bienestar social y Ley de Rescate Económico*, borrador para discusión del 30 de octubre de 2026, de 15 páginas. Daniel Wills compartió el documento y once imágenes en Mesa Fiscal el 1 de noviembre. La diapositiva da crédito al autor y usa los datos de su tabla 1, página 8, no una digitalización de las imágenes.

La gráfica compara la devolución plena con la restringida a compras con factura. Los deciles son de gasto por persona y el denominador del cambio es el mayor entre ingreso disponible y gasto del hogar. Los valores exactos de la tabla se conservan en JSON y CSV. La gráfica redondea a una cifra decimal.

El cotejo independiente del PDF contra JSON, CSV y coordenadas arroja 60 PASS y 0 FAIL. Para repetirlo:

```sh
python quality_reports/verificar_deciles.py /ruta/Bienestar.pdf
```

Confianza High sobre la transcripción. Confianza Medium sobre su lectura como aproximación a la incidencia económica. Es una simulación calibrada, no una observación de resultados. No se replicaron los microdatos. El modelo aproxima la elegibilidad por decil y la factura por lugar de compra, supone empleo y cantidades constantes y atribuye toda la mayor cotización patronal al trabajador. No simula el mínimo para pobreza extrema ni descuenta la devolución vigente. Tampoco incluye recortes de gasto ni rebajas empresariales. Estos límites aparecen en el anexo.

## PDF y conservación

Se verificaron las diapositivas nuevas y sus contiguas, la legibilidad, el orden y los créditos. El PDF tiene 22 páginas, 19 principales y tres anexos. La compilación final no reporta desbordamientos ni caracteres faltantes. El proceso conserva el aviso ambiental conocido de Fontconfig.

La comprobación numérica del resto de la presentación mantiene 144 PASS y 0 FAIL. Los documentos e imágenes originales se conservan solo en el archivo local de fuentes del seguimiento. No se incluyen en el repositorio público.
