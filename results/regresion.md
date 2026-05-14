# Regresion polinomial (entregable 5c)

Se ajustan polinomios de grado 1 a 5 sobre los tiempos medidos en
`results/tiempos.csv`. Para cada grado se reporta el coeficiente de
determinacion R^2 para ver cual ajusta mejor.

## FFD (greedy)

| grado | R^2 | coeficientes (mayor a menor) |
|---|---|---|
| 1 | 0.7278 | [2.871e-07, -8.42e-07] |
| 2 | 0.7382 | [7.6e-09, 9.56e-08, 1.979e-07] |
| 3 | 0.7384 | [-3e-10, 1.93e-08, -3.72e-08, 6.38e-07] |
| 4 | 0.7391 | [-1e-10, 6.4e-09, -9.97e-08, 8.244e-07, -1.4767e-06] |
| 5 | 0.7391 | [-0.0, -0.0, 4.1e-09, -7.3e-08, 6.805e-07, -1.1887e-06] |

**Mejor ajuste FFD: grado 5, R^2 = 0.7391.**

La teoria predice O(n log n + n^2) ≈ O(n^2) para la implementacion
ingenua. El ajuste cuadratico suele dar muy buen R^2, lo que concuerda
con el analisis del docs/04-complejidad.md.

## DP exacta

| grado | R^2 | coeficientes (mayor a menor) |
|---|---|---|
| 1 | 0.3618 | [4.3983843029, -42.4010923459] |
| 2 | 0.6822 | [0.9183233342, -18.766733254, 83.3615308291] |
| 3 | 0.8643 | [0.1719043704, -5.5066370751, 53.9695591966, -157.8375173343] |
| 4 | 0.9282 | [0.0289739814, -1.2814047696, 20.1266448543, -131.5518084528, 297.5046840313] |
| 5 | 0.9411 | [0.0042406452, -0.2397247244, 5.2264233221, -54.6050507295, 271.452207294, -508.9622637109] |

**Mejor ajuste polinomial DP: grado 5, R^2 = 0.9411.**

Un polinomio de grado alto puede dar R^2 razonable, pero la DP no es
polinomial sino exponencial. Para verlo mejor se ajusta log(t) = a·n + b:

- pendiente a = 1.0772
- t ≈ 4.2487e-08 · 2.9365^n

La base empirica (2.9365) se compara con el 3 teorico del analisis
asintotico O(3^n). Constantes y overhead de Python explican la
diferencia entre ambos valores.

## Calidad de la solucion greedy

- Ratio promedio FFD/OPT: **1.0087**
- Ratio maximo FFD/OPT: **1.2500**

La cota teorica conocida es FFD ≤ (11/9)·OPT + 6/9 ≈ 1.222·OPT + 0.667.
Los ratios medidos quedan por debajo de esa cota, como se esperaba.
