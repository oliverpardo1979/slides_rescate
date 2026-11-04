# Registro de comprobaciones numéricas

Historial acumulativo. Las correcciones se registran como nuevas corridas.

## 2026-11-03T18:14:50.715651+00:00 — inicial, base456b4a6

47 PASS, 1 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.35 | 2.35 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2028 | 3.58 | 3.58 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2029 | 3.87 | 3.87 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2030 | 4.09 | 4.09 | PDF oficial p204, fila efecto de la ley | PASS |
| FISCAL_gasto_neto_2027 | 0.58 | 0.58 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_gasto_neto_2027 | 0.58 | 0.58 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_gasto_neto_2030 | 0.81 | 0.81 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_gasto_neto_2030 | 0.81 | 0.81 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_financiacion_social_2027 | 1.46 | 1.46 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_financiacion_social_2027 | 1.46 | 1.46 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_financiacion_social_2030 | 1.38 | 1.38 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_financiacion_social_2030 | 1.38 | 1.38 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_otros_efectos_netos_2027 | 0.31 | 0.31 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_otros_efectos_netos_2027 | 0.31 | 0.31 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_otros_efectos_netos_2030 | 1.90 | 1.90 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_otros_efectos_netos_2030 | 1.90 | 1.90 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_total_ley_2027 | 2.35 | 2.35 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_total_ley_2030 | 4.09 | 4.09 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 24.39024390243902439024390244 | 25 | Anchos de segmentos TikZ,1de4puntos | FAIL |
## 2026-11-03T18:21:03.559424+00:00 — final, base456b4a6

48 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.35 | 2.35 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2028 | 3.58 | 3.58 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2029 | 3.87 | 3.87 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2030 | 4.09 | 4.09 | PDF oficial p204, fila efecto de la ley | PASS |
| FISCAL_gasto_neto_2027 | 0.58 | 0.58 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_gasto_neto_2027 | 0.58 | 0.58 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_gasto_neto_2030 | 0.81 | 0.81 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_gasto_neto_2030 | 0.81 | 0.81 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_financiacion_social_2027 | 1.46 | 1.46 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_financiacion_social_2027 | 1.46 | 1.46 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_financiacion_social_2030 | 1.38 | 1.38 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_financiacion_social_2030 | 1.38 | 1.38 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_otros_efectos_netos_2027 | 0.31 | 0.31 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_otros_efectos_netos_2027 | 0.31 | 0.31 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_otros_efectos_netos_2030 | 1.90 | 1.90 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_otros_efectos_netos_2030 | 1.90 | 1.90 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_total_ley_2027 | 2.35 | 2.35 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_total_ley_2030 | 4.09 | 4.09 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T20:24:32.506639+00:00 — formato_academico, base456b4a6

48 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.35 | 2.35 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2028 | 3.58 | 3.58 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2029 | 3.87 | 3.87 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2030 | 4.09 | 4.09 | PDF oficial p204, fila efecto de la ley | PASS |
| FISCAL_gasto_neto_2027 | 0.58 | 0.58 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_gasto_neto_2027 | 0.58 | 0.58 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_gasto_neto_2030 | 0.81 | 0.81 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_gasto_neto_2030 | 0.81 | 0.81 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_financiacion_social_2027 | 1.46 | 1.46 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_financiacion_social_2027 | 1.46 | 1.46 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_financiacion_social_2030 | 1.38 | 1.38 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_financiacion_social_2030 | 1.38 | 1.38 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_otros_efectos_netos_2027 | 0.31 | 0.31 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_otros_efectos_netos_2027 | 0.31 | 0.31 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_otros_efectos_netos_2030 | 1.90 | 1.90 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_otros_efectos_netos_2030 | 1.90 | 1.90 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_total_ley_2027 | 2.35 | 2.35 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| FISCAL_total_ley_2030 | 4.09 | 4.09 | Suma de filas del PDF p204. Otros efectos = residual. | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | data/ajuste_oficial.json contra sumas del PDF p204 | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T21:22:40.173637+00:00 — desagregacion_ajuste, base 0ecaa6648b49f4a779e6b8280322dec07aec7a24

154 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.35 | 2.35 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2028 | 3.58 | 3.58 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2029 | 3.87 | 3.87 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2030 | 4.09 | 4.09 | PDF oficial p204, fila efecto de la ley | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.39 | 0.39 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.31 | 0.31 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_personal_2027 | 0.00 | 0.00 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_personal_2030 | 0.52 | 0.52 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ops_2027 | 0.19 | 0.19 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ops_2030 | 0.18 | 0.18 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_sgp_2027 | 0.00 | 0.00 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_sgp_2030 | -0.20 | -0.20 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.56 | 0.56 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.45 | 0.45 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.27 | 0.27 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.24 | 0.24 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_impuestos_salud_2027 | 0.49 | 0.49 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_impuestos_salud_2030 | 0.54 | 0.54 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_iva_neto_2027 | 0.17 | 0.17 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_iva_neto_2030 | 1.06 | 1.06 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_renta_personas_2027 | 0.13 | 0.13 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_renta_personas_2030 | 0.57 | 0.57 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.05 | 0.05 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.21 | 0.21 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_normalizacion_2027 | 0.12 | 0.12 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_normalizacion_2030 | 0.00 | 0.00 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.24 | -0.24 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.47 | -0.47 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ccf_2027 | 0.14 | 0.14 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ccf_2030 | 0.15 | 0.15 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_efectos_macro_2027 | 0.08 | 0.08 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_efectos_macro_2030 | 0.54 | 0.54 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_diferencia_suma_2027 | 0.00 | 0.00 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_diferencia_suma_2030 | -0.01 | -0.01 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_total_ley_2027 | 2.35 | 2.35 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_total_ley_2030 | 4.09 | 4.09 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_menor_gasto_neto_2027 | 0.58 | 0.58 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_menor_gasto_neto_2030 | 0.81 | 0.81 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_cotizaciones_2027 | 0.83 | 0.83 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_2030 | 0.69 | 0.69 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_ingresos_medidas_2027 | 1.55 | 1.55 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ingresos_medidas_2030 | 2.60 | 2.60 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T21:25:45.550746+00:00 — desagregacion_final, base ec2f6781853a124a0dfa304262a001d1f2f23156

154 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.35 | 2.35 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2028 | 3.58 | 3.58 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2029 | 3.87 | 3.87 | PDF oficial p204, fila efecto de la ley | PASS |
| GRAFICO_2030 | 4.09 | 4.09 | PDF oficial p204, fila efecto de la ley | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.39 | 0.39 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.31 | 0.31 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_personal_2027 | 0.00 | 0.00 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_personal_2030 | 0.52 | 0.52 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ops_2027 | 0.19 | 0.19 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ops_2030 | 0.18 | 0.18 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_sgp_2027 | 0.00 | 0.00 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_sgp_2030 | -0.20 | -0.20 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.56 | 0.56 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.45 | 0.45 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.27 | 0.27 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.24 | 0.24 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_impuestos_salud_2027 | 0.49 | 0.49 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_impuestos_salud_2030 | 0.54 | 0.54 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_iva_neto_2027 | 0.17 | 0.17 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_iva_neto_2030 | 1.06 | 1.06 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_renta_personas_2027 | 0.13 | 0.13 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_renta_personas_2030 | 0.57 | 0.57 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.05 | 0.05 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.21 | 0.21 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_normalizacion_2027 | 0.12 | 0.12 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_normalizacion_2030 | 0.00 | 0.00 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.24 | -0.24 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.47 | -0.47 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ccf_2027 | 0.14 | 0.14 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ccf_2030 | 0.15 | 0.15 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_efectos_macro_2027 | 0.08 | 0.08 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_efectos_macro_2030 | 0.54 | 0.54 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_diferencia_suma_2027 | 0.00 | 0.00 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_diferencia_suma_2030 | -0.01 | -0.01 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_total_ley_2027 | 2.35 | 2.35 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_total_ley_2030 | 4.09 | 4.09 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_menor_gasto_neto_2027 | 0.58 | 0.58 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_menor_gasto_neto_2030 | 0.81 | 0.81 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_cotizaciones_2027 | 0.83 | 0.83 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_cotizaciones_2030 | 0.69 | 0.69 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_ingresos_medidas_2027 | 1.55 | 1.55 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| FISCAL_ingresos_medidas_2030 | 2.60 | 2.60 | TeX y PDF de diapositivas contra sumas del PDF oficial p204 | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T21:28:06.177595+00:00 — un_decimal, base bd656fbc054811d73ed28226be9c49b5aedffacc

152 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_menor_gasto_neto_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_menor_gasto_neto_2030 | 0.8 | 0.8 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_cotizaciones_2027 | 0.8 | 0.8 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_2030 | 0.7 | 0.7 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_impuestos_y_gestion_netos_2027 | 0.7 | 0.7 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_y_gestion_netos_2030 | 1.9 | 1.9 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_ingresos_medidas_2027 | 1.6 | 1.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ingresos_medidas_2030 | 2.6 | 2.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T21:34:53.908146+00:00 — orden_colores, base 25931a51764bc294f9ebb3088dd06d87a314ee69

160 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_principal_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_principal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_principal_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_principal_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_principal_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_principal_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_principal_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_principal_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_principal_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_principal_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_principal_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_principal_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_2027 | 0.8 | 0.8 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_2030 | 0.7 | 0.7 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_ingresos_medidas_2027 | 1.6 | 1.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ingresos_medidas_2030 | 2.6 | 2.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T21:36:30.690936+00:00 — orden_colores_final, base 25931a51764bc294f9ebb3088dd06d87a314ee69

164 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_principal_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_principal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_principal_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_principal_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_principal_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_principal_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_principal_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_principal_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_principal_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_principal_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_principal_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_principal_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_2027 | 0.8 | 0.8 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_2030 | 0.7 | 0.7 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_cotizaciones_detalle_2027 | 0.8 | 0.8 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_detalle_2030 | 0.7 | 0.7 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_y_gestion_netos_detalle_2027 | 0.7 | 0.7 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_y_gestion_netos_detalle_2030 | 1.9 | 1.9 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ingresos_medidas_2027 | 1.6 | 1.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ingresos_medidas_2030 | 2.6 | 2.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T21:38:09.025302+00:00 — orden_colores_final, base 25931a51764bc294f9ebb3088dd06d87a314ee69

164 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_principal_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_principal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_principal_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_principal_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_principal_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_principal_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_principal_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_principal_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_principal_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_principal_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_principal_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_principal_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_2027 | 0.8 | 0.8 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_2030 | 0.7 | 0.7 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| FISCAL_cotizaciones_detalle_2027 | 0.8 | 0.8 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_detalle_2030 | 0.7 | 0.7 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_y_gestion_netos_detalle_2027 | 0.7 | 0.7 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_y_gestion_netos_detalle_2030 | 1.9 | 1.9 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ingresos_medidas_2027 | 1.6 | 1.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ingresos_medidas_2030 | 2.6 | 2.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T21:40:50.573743+00:00 — cuadro_unico, base d359e98c0ee93d0650cdbe7dcaa58254bb007146

144 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T21:57:38.912040+00:00 — orden_magnitud, base 950f68f8d08dd58818020e06835df99230cffa66

144 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T22:00:22.869516+00:00 — orden_magnitud_integrado, base cc1b50027d3890c9f91a972658c1c83f27d25635

144 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-03T22:25:07.530785+00:00 — iva_deciles_20261103, base bce461a52cf2e7a401870c033e38c7a958adb58b

144 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-04T12:07:22.893781+00:00 — efectiva_requisitos_20261104, base 190595f367df2f54c8d3b4ed4e3f13c437990780

144 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-04T12:15:35.584717+00:00 — crisis_apertura_20261104, base ab38ce83a5fdb8f7a45fc4271cabc350cd5b609e

144 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
## 2026-11-04T12:39:45.803576+00:00 — tabla_ingreso_nunez_20261104, base 9d5cbbbbe0a04d8a04087107691d92b831d540ef

144 PASS, 0 FAIL.

| Afirmación | Mostrado | Recalculado | Método | Resultado |
|---|---:|---:|---|---|
| COP_UVTpesos | 52374 | 52374 | UVT2026 según resolución238/2025 | PASS |
| COP_SMpesos | 1750905 | 1750905 | SMLMV2026 según decreto159/2026 | PASS |
| COP_PisoAnual | 37709280 | 37709280 | 720*52374 | PASS |
| COP_PisoMensual | 3142440 | 3142440 | 720*52374/12 | PASS |
| COP_TechoAnual | 57087660 | 57087660 | 1090*52374 | PASS |
| COP_TechoMensual | 4757305 | 4757305 | 1090*52374/12 | PASS |
| COP_EjemploImpuesto | 848459 | 848459 | (900-720)*0.09*52374 | PASS |
| COP_EjemploMes | 70705 | 70705 | (900-720)*0.09*52374/12 | PASS |
| COP_ExentaAntes | 41375460 | 41375460 | 790*52374 | PASS |
| COP_ExentaDespues | 32995620 | 32995620 | 630*52374 | PASS |
| COP_Dependiente | 3770928 | 3770928 | 72*52374 | PASS |
| COP_SalarioEjemplo | 7003620 | 7003620 | 4*1750905 | PASS |
| COP_SaludAntes | 280145 | 280145 | 4*1750905*0.04 | PASS |
| COP_SaludDespues | 385199 | 385199 | 4*1750905*0.055 | PASS |
| COP_SaludDiferencia | 105054 | 105054 | 4*1750905*(0.055-0.04), solo aporte a salud | PASS |
| COP_EmpresaTotal | 945489 | 945489 | 4*1750905*(0.085+0.02+0.03) | PASS |
| COP_DevolucionTope | 288057 | 288057 | 5.5*52374 | PASS |
| GRAFICO_2027 | 2.4 | 2.4 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2028 | 3.6 | 3.6 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2029 | 3.9 | 3.9 | PDF oficial p204, redondeado a un decimal | PASS |
| GRAFICO_2030 | 4.1 | 4.1 | PDF oficial p204, redondeado a un decimal | PASS |
| FILAS_SIN_DOBLE_CONTEO | 20 | 20 | Cada medida fuente se utiliza una sola vez | PASS |
| COBERTURA_DE_MEDIDAS | 20 | 20 | Cotejo exhaustivo de filas de medidas, sin subtotales ni estrategia adicional | PASS |
| SALIDA_eficiencia_gasto_2027 | 0.39 | 0.39 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2027 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2027 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2027 | 0.27 | 0.27 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2027 | 0.49 | 0.49 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2027 | 0.17 | 0.17 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2027 | 0.13 | 0.13 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2027 | 0.05 | 0.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2027 | 0.12 | 0.12 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2027 | -0.24 | -0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2027 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2027 | 0.08 | 0.08 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2027 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2027 | 2.35 | 2.35 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2027 | 2.35 | 2.35 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2028 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2028 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2028 | 0.19 | 0.19 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2028 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2028 | 0.41 | 0.41 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2028 | 0.53 | 0.53 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2028 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2028 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2028 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2028 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2028 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2028 | 0.14 | 0.14 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2028 | 0.23 | 0.23 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2028 | -0.02 | -0.02 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2028 | 3.58 | 3.58 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2028 | 3.58 | 3.58 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2029 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2029 | 0.47 | 0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2029 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2029 | -0.10 | -0.10 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2029 | 0.44 | 0.44 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2029 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2029 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2029 | 1.05 | 1.05 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2029 | 0.56 | 0.56 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2029 | 0.20 | 0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2029 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2029 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2029 | 0.30 | 0.30 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2029 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2029 | 3.87 | 3.87 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2029 | 3.87 | 3.87 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| SALIDA_eficiencia_gasto_2030 | 0.31 | 0.31 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_personal_2030 | 0.52 | 0.52 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ops_2030 | 0.18 | 0.18 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_sgp_2030 | -0.20 | -0.20 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_empleador_2030 | 0.45 | 0.45 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_cotizaciones_personas_2030 | 0.24 | 0.24 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_impuestos_salud_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_iva_neto_2030 | 1.06 | 1.06 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_renta_personas_2030 | 0.57 | 0.57 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_otros_impuestos_gestion_2030 | 0.21 | 0.21 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_normalizacion_2030 | 0.00 | 0.00 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_rebajas_tributarias_2030 | -0.47 | -0.47 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_ccf_2030 | 0.15 | 0.15 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_efectos_macro_2030 | 0.54 | 0.54 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_diferencia_suma_2030 | -0.01 | -0.01 | Filas identificadas de la página 204 del PDF oficial | PASS |
| SALIDA_total_ley_2030 | 4.09 | 4.09 | Filas identificadas de la página 204 del PDF oficial | PASS |
| CONCILIACION_2030 | 4.09 | 4.09 | Suma de todas las medidas y diferencia publicada, sin duplicación | PASS |
| FISCAL_eficiencia_gasto_2027 | 0.4 | 0.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_eficiencia_gasto_2030 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_personal_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ops_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2027 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_sgp_2030 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2027 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_empleador_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2027 | 0.3 | 0.3 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_cotizaciones_personas_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2027 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_impuestos_salud_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2027 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_iva_neto_2030 | 1.1 | 1.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_renta_personas_2030 | 0.6 | 0.6 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_otros_impuestos_gestion_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_normalizacion_2030 | 0.0 | 0.0 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2027 | -0.2 | -0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_rebajas_tributarias_2030 | -0.5 | -0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_ccf_2030 | 0.2 | 0.2 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2027 | 0.1 | 0.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_efectos_macro_2030 | 0.5 | 0.5 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2027 | 2.4 | 2.4 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| FISCAL_total_ley_2030 | 4.1 | 4.1 | TeX y PDF contra sumas del PDF oficial p204, redondeadas a un decimal | PASS |
| RESUMEN_menor_gasto_neto_2027 | 0.58 | 0.58 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2028 | 0.73 | 0.73 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2029 | 0.86 | 0.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_menor_gasto_neto_2030 | 0.81 | 0.81 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2027 | 0.83 | 0.83 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2028 | 0.64 | 0.64 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2029 | 0.68 | 0.68 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_cotizaciones_2030 | 0.69 | 0.69 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2027 | 0.72 | 0.72 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2028 | 1.86 | 1.86 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2029 | 1.88 | 1.88 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RESUMEN_impuestos_y_gestion_netos_2030 | 1.91 | 1.91 | Agrupación por mecanismo desde el PDF oficial | PASS |
| RUGE_8140000 | 426.3 | 426.3 | 8140000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_5530000 | 289.6 | 289.6 | 5530000*52374/1e9, redondeado a0.1 | PASS |
| RUGE_2580000 | 135.1 | 135.1 | 2580000*52374/1e9, redondeado a0.1 | PASS |
| UMBRAL95 | 104748 | 104748 | 2e6*52374/1e6; millones COP | PASS |
| PRECIO_IVA5 | 105000 | 105000.00 | 100000*1.05 | PASS |
| PRECIO_IVA19 | 119000 | 119000.00 | 100000*1.19 | PASS |
| VAR_PRECIO_IVA | 13.3 | 13.33333333333333333333333330 | (119/105-1)*100 | PASS |
| RENTA_EMPRESA35 | 350 | 350.00 | 1000*0.35, millonesCOP | PASS |
| RENTA_EMPRESA31 | 310 | 310.00 | 1000*0.31, millonesCOP | PASS |
| NORMALIZACION15 | 150 | 150.00 | 1000*0.15, millonesCOP | PASS |
| DIAGRAMA_CAJAS | 25.00 | 25 | Anchos de segmentos TikZ,1de4puntos | PASS |
