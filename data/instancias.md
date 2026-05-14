# Listado de instancias de prueba (entregable 5a)

Estas son las instancias generadas por `src/generator.py` y que se usan en el
benchmark para medir tiempos de ejecucion de DP y FFD. Cada una se identifica
con un `id` de la forma `n{N}-{distribucion}-s{semilla}`.

## Parametros generales

- Capacidad de cada bin: **C = 20** para las instancias aleatorias.
- Tamanios de entrada: **n ∈ {5, 8, 10, 12, 14, 16, 18, 20}**.
- Semillas usadas: **1, 2 y 3**.
- Total instancias aleatorias: 8 × 3 distribuciones × 3 semillas = **72**.
- Mas **3 instancias adversariales** fijas (C = 10) donde FFD se sabe que no
  encuentra el optimo. **Total general: 75 instancias.**

El tope en n = 20 viene del costo de la DP. Con O(3ⁿ), pasar de 20 ya tarda
varios minutos por instancia, asi que se respeta ese limite para que el
benchmark termine en tiempo razonable.

## Distribuciones usadas

| Distribucion | Rango de tamanios | Idea |
|---|---|---|
| uniforme | `[1, C]` | Caso general, mezcla de objetos chicos y grandes. |
| grandes | `[C/2, C]` | Cada objeto ocupa mas de la mitad del bin, casi siempre va uno por bin. |
| pequenos | `[1, C/4]` | Muchos objetos chicos, varios entran por bin. |

Las tres distribuciones se eligieron para forzar comportamientos distintos:
en `grandes` la solucion optima esta cerca de `n` bins, en `pequenos` esta
cerca de la cota de volumen, y `uniforme` queda en medio. Asi se observa si
el greedy FFD se acerca al optimo en distintos escenarios.

## Tabla de instancias

| id | n | C | distribucion | semilla | suma_total | items |
|---|---|---|---|---|---|---|
| n05-uniforme-s1 | 5 | 20 | uniforme | 1 | 40 | [5, 19, 3, 9, 4] |
| n05-uniforme-s2 | 5 | 20 | uniforme | 2 | 26 | [2, 3, 3, 12, 6] |
| n05-uniforme-s3 | 5 | 20 | uniforme | 3 | 62 | [8, 19, 18, 5, 12] |
| n05-grandes-s1 | 5 | 20 | grandes | 1 | 67 | [12, 19, 11, 14, 11] |
| n05-grandes-s2 | 5 | 20 | grandes | 2 | 59 | [10, 11, 11, 15, 12] |
| n05-grandes-s3 | 5 | 20 | grandes | 3 | 77 | [13, 19, 18, 12, 15] |
| n05-pequenos-s1 | 5 | 20 | pequenos | 1 | 12 | [2, 5, 1, 3, 1] |
| n05-pequenos-s2 | 5 | 20 | pequenos | 2 | 8 | [1, 1, 1, 3, 2] |
| n05-pequenos-s3 | 5 | 20 | pequenos | 3 | 17 | [2, 5, 5, 2, 3] |
| n08-uniforme-s1 | 8 | 20 | uniforme | 1 | 87 | [5, 19, 3, 9, 4, 16, 15, 16] |
| n08-uniforme-s2 | 8 | 20 | uniforme | 2 | 65 | [2, 3, 3, 12, 6, 10, 9, 20] |
| n08-uniforme-s3 | 8 | 20 | uniforme | 3 | 117 | [8, 19, 18, 5, 12, 20, 16, 19] |
| n08-grandes-s1 | 8 | 20 | grandes | 1 | 118 | [12, 19, 11, 14, 11, 17, 17, 17] |
| n08-grandes-s2 | 8 | 20 | grandes | 2 | 107 | [10, 11, 11, 15, 12, 20, 14, 14] |
| n08-grandes-s3 | 8 | 20 | grandes | 3 | 133 | [13, 19, 18, 12, 15, 19, 17, 20] |
| n08-pequenos-s1 | 8 | 20 | pequenos | 1 | 24 | [2, 5, 1, 3, 1, 4, 4, 4] |
| n08-pequenos-s2 | 8 | 20 | pequenos | 2 | 19 | [1, 1, 1, 3, 2, 3, 3, 5] |
| n08-pequenos-s3 | 8 | 20 | pequenos | 3 | 31 | [2, 5, 5, 2, 3, 5, 4, 5] |
| n10-uniforme-s1 | 10 | 20 | uniforme | 1 | 107 | [5, 19, 3, 9, 4, 16, 15, 16, 13, 7] |
| n10-uniforme-s2 | 10 | 20 | uniforme | 2 | 92 | [2, 3, 3, 12, 6, 10, 9, 20, 7, 20] |
| n10-uniforme-s3 | 10 | 20 | uniforme | 3 | 140 | [8, 19, 18, 5, 12, 20, 16, 19, 3, 20] |
| n10-grandes-s1 | 10 | 20 | grandes | 1 | 154 | [12, 19, 11, 14, 11, 17, 17, 17, 20, 16] |
| n10-grandes-s2 | 10 | 20 | grandes | 2 | 139 | [10, 11, 11, 15, 12, 20, 14, 14, 19, 13] |
| n10-grandes-s3 | 10 | 20 | grandes | 3 | 163 | [13, 19, 18, 12, 15, 19, 17, 20, 19, 11] |
| n10-pequenos-s1 | 10 | 20 | pequenos | 1 | 30 | [2, 5, 1, 3, 1, 4, 4, 4, 4, 2] |
| n10-pequenos-s2 | 10 | 20 | pequenos | 2 | 26 | [1, 1, 1, 3, 2, 3, 3, 5, 2, 5] |
| n10-pequenos-s3 | 10 | 20 | pequenos | 3 | 37 | [2, 5, 5, 2, 3, 5, 4, 5, 1, 5] |
| n12-uniforme-s1 | 12 | 20 | uniforme | 1 | 127 | [5, 19, 3, 9, 4, 16, 15, 16, 13, 7, 4, 16] |
| n12-uniforme-s2 | 12 | 20 | uniforme | 2 | 113 | [2, 3, 3, 12, 6, 10, 9, 20, 7, 20, 2, 19] |
| n12-uniforme-s3 | 12 | 20 | uniforme | 3 | 157 | [8, 19, 18, 5, 12, 20, 16, 19, 3, 20, 1, 16] |
| n12-grandes-s1 | 12 | 20 | grandes | 1 | 178 | [12, 19, 11, 14, 11, 17, 17, 17, 20, 16, 13, 11] |
| n12-grandes-s2 | 12 | 20 | grandes | 2 | 168 | [10, 11, 11, 15, 12, 20, 14, 14, 19, 13, 19, 10] |
| n12-grandes-s3 | 12 | 20 | grandes | 3 | 192 | [13, 19, 18, 12, 15, 19, 17, 20, 19, 11, 19, 10] |
| n12-pequenos-s1 | 12 | 20 | pequenos | 1 | 35 | [2, 5, 1, 3, 1, 4, 4, 4, 4, 2, 1, 4] |
| n12-pequenos-s2 | 12 | 20 | pequenos | 2 | 32 | [1, 1, 1, 3, 2, 3, 3, 5, 2, 5, 1, 5] |
| n12-pequenos-s3 | 12 | 20 | pequenos | 3 | 42 | [2, 5, 5, 2, 3, 5, 4, 5, 1, 5, 1, 4] |
| n14-uniforme-s1 | 14 | 20 | uniforme | 1 | 141 | [5, 19, 3, 9, 4, 16, 15, 16, 13, 7, 4, 16, 1, 13] |
| n14-uniforme-s2 | 14 | 20 | uniforme | 2 | 133 | [2, 3, 3, 12, 6, 10, 9, 20, 7, 20, 2, 19, 6, 14] |
| n14-uniforme-s3 | 14 | 20 | uniforme | 3 | 184 | [8, 19, 18, 5, 12, 20, 16, 19, 3, 20, 1, 16, 9, 18] |
| n14-grandes-s1 | 14 | 20 | grandes | 1 | 205 | [12, 19, 11, 14, 11, 17, 17, 17, 20, 16, 13, 11, 17, 10] |
| n14-grandes-s2 | 14 | 20 | grandes | 2 | 207 | [10, 11, 11, 15, 12, 20, 14, 14, 19, 13, 19, 10, 19, 20] |
| n14-grandes-s3 | 14 | 20 | grandes | 3 | 223 | [13, 19, 18, 12, 15, 19, 17, 20, 19, 11, 19, 10, 17, 14] |
| n14-pequenos-s1 | 14 | 20 | pequenos | 1 | 40 | [2, 5, 1, 3, 1, 4, 4, 4, 4, 2, 1, 4, 1, 4] |
| n14-pequenos-s2 | 14 | 20 | pequenos | 2 | 38 | [1, 1, 1, 3, 2, 3, 3, 5, 2, 5, 1, 5, 2, 4] |
| n14-pequenos-s3 | 14 | 20 | pequenos | 3 | 50 | [2, 5, 5, 2, 3, 5, 4, 5, 1, 5, 1, 4, 3, 5] |
| n16-uniforme-s1 | 16 | 20 | uniforme | 1 | 175 | [5, 19, 3, 9, 4, 16, 15, 16, 13, 7, 4, 16, 1, 13, 14, 20] |
| n16-uniforme-s2 | 16 | 20 | uniforme | 2 | 163 | [2, 3, 3, 12, 6, 10, 9, 20, 7, 20, 2, 19, 6, 14, 13, 17] |
| n16-uniforme-s3 | 16 | 20 | uniforme | 3 | 199 | [8, 19, 18, 5, 12, 20, 16, 19, 3, 20, 1, 16, 9, 18, 8, 7] |
| n16-grandes-s1 | 16 | 20 | grandes | 1 | 237 | [12, 19, 11, 14, 11, 17, 17, 17, 20, 16, 13, 11, 17, 10, 16, 16] |
| n16-grandes-s2 | 16 | 20 | grandes | 2 | 235 | [10, 11, 11, 15, 12, 20, 14, 14, 19, 13, 19, 10, 19, 20, 12, 16] |
| n16-grandes-s3 | 16 | 20 | grandes | 3 | 254 | [13, 19, 18, 12, 15, 19, 17, 20, 19, 11, 19, 10, 17, 14, 18, 13] |
| n16-pequenos-s1 | 16 | 20 | pequenos | 1 | 49 | [2, 5, 1, 3, 1, 4, 4, 4, 4, 2, 1, 4, 1, 4, 4, 5] |
| n16-pequenos-s2 | 16 | 20 | pequenos | 2 | 47 | [1, 1, 1, 3, 2, 3, 3, 5, 2, 5, 1, 5, 2, 4, 4, 5] |
| n16-pequenos-s3 | 16 | 20 | pequenos | 3 | 54 | [2, 5, 5, 2, 3, 5, 4, 5, 1, 5, 1, 4, 3, 5, 2, 2] |
| n18-uniforme-s1 | 18 | 20 | uniforme | 1 | 191 | [5, 19, 3, 9, 4, 16, 15, 16, 13, 7, 4, 16, 1, 13, 14, 20, 1, 15] |
| n18-uniforme-s2 | 18 | 20 | uniforme | 2 | 193 | [2, 3, 3, 12, 6, 10, 9, 20, 7, 20, 2, 19, 6, 14, 13, 17, 12, 18] |
| n18-uniforme-s3 | 18 | 20 | uniforme | 3 | 233 | [8, 19, 18, 5, 12, 20, 16, 19, 3, 20, 1, 16, 9, 18, 8, 7, 16, 18] |
| n18-grandes-s1 | 18 | 20 | grandes | 1 | 266 | [12, 19, 11, 14, 11, 17, 17, 17, 20, 16, 13, 11, 17, 10, 16, 16, 19, 10] |
| n18-grandes-s2 | 18 | 20 | grandes | 2 | 271 | [10, 11, 11, 15, 12, 20, 14, 14, 19, 13, 19, 10, 19, 20, 12, 16, 20, 16] |
| n18-grandes-s3 | 18 | 20 | grandes | 3 | 284 | [13, 19, 18, 12, 15, 19, 17, 20, 19, 11, 19, 10, 17, 14, 18, 13, 13, 17] |
| n18-pequenos-s1 | 18 | 20 | pequenos | 1 | 54 | [2, 5, 1, 3, 1, 4, 4, 4, 4, 2, 1, 4, 1, 4, 4, 5, 1, 4] |
| n18-pequenos-s2 | 18 | 20 | pequenos | 2 | 55 | [1, 1, 1, 3, 2, 3, 3, 5, 2, 5, 1, 5, 2, 4, 4, 5, 3, 5] |
| n18-pequenos-s3 | 18 | 20 | pequenos | 3 | 63 | [2, 5, 5, 2, 3, 5, 4, 5, 1, 5, 1, 4, 3, 5, 2, 2, 4, 5] |
| n20-uniforme-s1 | 20 | 20 | uniforme | 1 | 208 | [5, 19, 3, 9, 4, 16, 15, 16, 13, 7, 4, 16, 1, 13, 14, 20, 1, 15, 9, 8] |
| n20-uniforme-s2 | 20 | 20 | uniforme | 2 | 225 | [2, 3, 3, 12, 6, 10, 9, 20, 7, 20, 2, 19, 6, 14, 13, 17, 12, 18, 15, 17] |
| n20-uniforme-s3 | 20 | 20 | uniforme | 3 | 267 | [8, 19, 18, 5, 12, 20, 16, 19, 3, 20, 1, 16, 9, 18, 8, 7, 16, 18, 18, 16] |
| n20-grandes-s1 | 20 | 20 | grandes | 1 | 297 | [12, 19, 11, 14, 11, 17, 17, 17, 20, 16, 13, 11, 17, 10, 16, 16, 19, 10, 17, 14] |
| n20-grandes-s2 | 20 | 20 | grandes | 2 | 304 | [10, 11, 11, 15, 12, 20, 14, 14, 19, 13, 19, 10, 19, 20, 12, 16, 20, 16, 18, 15] |
| n20-grandes-s3 | 20 | 20 | grandes | 3 | 320 | [13, 19, 18, 12, 15, 19, 17, 20, 19, 11, 19, 10, 17, 14, 18, 13, 13, 17, 18, 18] |
| n20-pequenos-s1 | 20 | 20 | pequenos | 1 | 59 | [2, 5, 1, 3, 1, 4, 4, 4, 4, 2, 1, 4, 1, 4, 4, 5, 1, 4, 3, 2] |
| n20-pequenos-s2 | 20 | 20 | pequenos | 2 | 64 | [1, 1, 1, 3, 2, 3, 3, 5, 2, 5, 1, 5, 2, 4, 4, 5, 3, 5, 4, 5] |
| n20-pequenos-s3 | 20 | 20 | pequenos | 3 | 72 | [2, 5, 5, 2, 3, 5, 4, 5, 1, 5, 1, 4, 3, 5, 2, 2, 4, 5, 5, 4] |

## Instancias adversariales

Tres casos hardcodeados con capacidad C = 10. Son contraejemplos conocidos
donde FFD no logra el optimo (ratio FFD/OPT > 1). Se incluyen para que el
benchmark muestre que la cota teorica 11/9·OPT + 6/9 si se acerca a llenarse
en algunas instancias y no se quede solo en ratio = 1.

| id | n | C | distribucion | suma_total | items | FFD | OPT | ratio |
|---|---|---|---|---|---|---|---|---|
| n10-adversarial-1 | 10 | 10 | adversarial | 39 | [5, 5, 5, 4, 4, 4, 3, 3, 3, 3] | 5 | 4 | 1.25 |
| n12-adversarial-2 | 12 | 10 | adversarial | 50 | [7, 7, 5, 5, 4, 4, 3, 3, 3, 3, 3, 3] | 6 | 5 | 1.20 |
| n14-adversarial-3 | 14 | 10 | adversarial | 50 | [6, 6, 5, 5, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2] | 6 | 5 | 1.20 |

## Reproducibilidad

Para regenerar esta lista se pueden usar las funciones del modulo:

```python
from generator import all_instances, print_all_instances

print_all_instances()
```

Como las semillas son fijas, las instancias salen siempre con los mismos items.
