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
