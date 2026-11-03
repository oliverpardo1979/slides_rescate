# Meta Skill Review Oliver — Ley de Rescate

3 de noviembre de 2026. Versión inicial revisada: `456b4a6`. Presentación Beamer de 18 diapositivas y 2 anexos para público informado, sin conocimiento de la conversación.

## Diagnóstico y selección

La presentación tenía una primera verificación técnica y de cálculos. Correspondía una revisión acotada de comprensión, interpretación y correspondencia entre cifras y fuentes. Se aplicaron `lectura`, `referee2-cunningham` en modo deck con un revisor independiente y `audit-reproducibility-santanna` para los cálculos expuestos. Las tres estaban instaladas. `voz-oliver-pardo` orientó las reparaciones.

Prioridad alta para dirección del pago, alcance de los ejemplos y fuentes. Costo relativo bajo para lectura, medio para revisión independiente y cotejo numérico. Se reutilizaron los insumos y la auditoría documental existentes. No se ejecutaron una revisión econométrica, una réplica fiscal desde microdatos ni revisiones editoriales redundantes.

## Resultado y correcciones

El revisor independiente dictaminó **Minor Revisions** sobre la versión inicial y cubrió 20 de 20 diapositivas. Su informe original se conserva en el expediente local de revisión.

- En 7, el ejemplo ahora dice «aporte adicional a salud». El valor calculado no es una liquidación completa del ingreso disponible después de impuestos.
- En 8, el título dice que las empresas vuelven a pagar aportes. «Recuperan» permitía entender que recibían dinero.
- En 2–4, se hace visible la proyección de Hacienda, la unidad del cuadro, el ámbito de los recortes y la referencia a la meta de inflación para personal.
- En 10 y 15, se explica el fondo de protección al cesante y se identifica que los mínimos RUGE son inversión nueva. La proporción del dibujo de cajas quedó exactamente 1:3.
- En 16–17, se precisan los efectos de la normalización y condiciones del mecanismo de controversias. Ecopetrol y Reficar tienen disputas documentadas. La elegibilidad efectiva y el beneficio dependen del expediente.
- En 18, el cierre propone corregir preferencias injustificadas y asegurar una devolución del IVA operativa.
- En 19, el título ya no afirma crecimiento de facturación sin mostrar una serie temporal.
- Se condicionó `inputenc` al motor y se completaron enlaces a fuentes primarias. No se alteraron los valores de los ejemplos ni la selección de temas.

## Cifras y compilación

La primera auditoría dio 47 PASS y 1 FAIL: la diferencia estaba en el ancho de los bloques del dibujo de cajas, no en una conversión monetaria. La versión final dio **48 PASS y 0 FAIL**. Las comprobaciones abarcan conversiones, ejemplos, gráfico fiscal, cuadro agregado, sus salidas declaradas y proporción visual. Se conserva el historial de ambas corridas y el script. El cotejo reconstruye la agrupación desde la tabla 14 del PDF oficial.

El PDF final mantiene 20 páginas. Se renderizaron e inspeccionaron todas. El log de Tectonic/XeTeX no tiene avisos de LaTeX, desbordamientos ni caracteres faltantes. El ejecutable imprime una incidencia local de Fontconfig que no impidió renderizar ni provocó esos defectos. La compilación independiente del revisor no pudo realizarse por acceso a su caché de paquetes. Su dictamen técnico se basó en el PDF y el log iniciales, y no se presenta como recompilación independiente exitosa.

## Control de fuentes

Se extrajeron los enlaces del PDF y se comprobaron los ocho destinos primarios distintos: todos devolvieron HTTP 200. El proyecto conserva el SHA 256 `4a7e52938b91a30da837c41e3e6ad4a28e667d546aafac4add16892f5a6ef6cf`.

Se verificaron identidad, fecha, artículos/páginas y respaldo pertinente de las fuentes centrales: Hacienda/Cámara, DIAN, normativa y comunicados de Ecopetrol. Para este género se conservan citas jurídicas por institución, norma, artículo y página al pie. No se impuso autor–año ni una bibliografía académica separada. Los detalles y hashes de acceso constan en `fuentes_enlaces.json`. HTTP 200 acredita accesibilidad, no demuestra por sí solo el contenido de la cita.

## Límites y confianza

**High** sobre las correcciones de lectura y los cálculos aislados cotejados. La auditoría verifica lo expuesto, no certifica el ahorro fiscal neto desde microdatos, la cobertura efectiva de EfectIVA, el costo agregado de RUGE ni la elegibilidad final de empresas al artículo 95. El juicio de distribución sigue siendo una valoración identificable del autor. **Medium** sobre legibilidad a distancia, porque no se especificaron sala ni duración.

La presentación conserva 18 diapositivas principales y 2 anexos. La revisión y sus reparaciones están terminadas dentro de este alcance. La auditoría general del proyecto de ley continúa por separado.


## Actualización de formato solicitada por Oliver, 3 de noviembre

Referencia principal: `Again-Firm-Size-Paper/presentacion_javeriana.tex`, commit `3bc4cca`. Se compararon los PDF de tamaño de firma, tributación empresarial (mayo de 2024 y diciembre de 2025) y *El Laberinto Fiscal de Colombia*. Se adoptó el formato de tamaño de firma, con fuentes visibles por la naturaleza jurídica de esta presentación.

Se reemplazaron los porcentajes grandes de contratación y personal por dos viñetas. Se conservan las cifras, condiciones y orden. Las 20 páginas se renderizaron y revisaron. El log no presenta desbordamientos ni advertencias de LaTeX. El entorno vuelve a emitir el aviso de Fontconfig ya documentado, sin defecto visible de fuentes. Las 48 comprobaciones de la corrida `formato_academico` pasan. Esta actualización de diseño no constituye una nueva auditoría integral ni una segunda revisión independiente.


## Desagregación de gasto e ingresos solicitada por Oliver

Las diapositivas 3 y 4 sustituyen la agrupación anterior y su residuo «otros efectos netos». La 3 muestra menor gasto neto con eficiencia, personal, OPS y mayor SGP. Se distinguen las cotizaciones, los impuestos netos de rebajas, la reasignación de las cajas y los efectos macro. La 4 desagrega las cotizaciones y los impuestos. La presentación pasa a 19 diapositivas principales y dos anexos.

La clasificación cubre las 20 filas de medidas de la tabla 14 una vez cada una. No incorpora subtotales de la fuente, medidas externas a la ley ni enajenaciones en la suma del proyecto. Las cotizaciones son ingresos sociales que permiten sustituir transferencias de la Nación. Su efecto fiscal se cuenta una sola vez. La reasignación de cajas no es una nueva cotización. El IVA se conserva neto de EfectIVA. Los efectos macro y la gestión no son ingresos asegurados. La eficiencia sigue siendo una estimación oficial pendiente de contrastar con la ejecución.

En 2030, los recortes previstos suman 1,01 puntos del PIB y el mayor gasto SGP resta 0,20, dejando 0,81 de menor gasto neto. Las cotizaciones suman 0,69 y los impuestos netos 1,91. Los 2,60 de mayores ingresos se complementan con 0,15 de reasignación de cajas y 0,54 de efectos macro. Los componentes suman 4,10 frente al total publicado de 4,09. Se conserva −0,01 como diferencia de suma de las cifras publicadas redondeadas, sin atribuirla a una medida identificada. En 2028 hay una diferencia de −0,02. RUGE y artículo 95 no tienen costo separado en la tabla y no se presupone costo cero.

Cotejo contra el PDF oficial de la página 204: 154 PASS y 0 FAIL en `desagregacion_ajuste`. Incluye fuentes, agregaciones, salidas de las cuatro vigencias y cuadros del PDF. Se revisaron visualmente ambas diapositivas nuevas. La compilación final no presenta desbordamientos ni advertencias de LaTeX. No es una nueva revisión independiente ni una certificación del ahorro desde microdatos.


## Presentación con una cifra decimal

Por instrucción de Oliver, los cuadros de gasto e ingresos, el gráfico del ajuste y las referencias a puntos del PIB se muestran con una cifra decimal. Se retira del cuadro la fila de diferencias de suma. Los archivos de cálculo mantienen la precisión original, los totales se calculan antes de redondear y no se atribuye significado económico a diferencias pequeñas de presentación. Se revisaron ambos cuadros y la compilación, con 152 comprobaciones PASS y 0 FAIL en `un_decimal`.
