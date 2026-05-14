# Proyecto #2 — Bin Packing Problem

**CC3894 – Análisis y Diseño de Algoritmos**
Universidad del Valle de Guatemala · Semestre 1, 2026
Docente: Ing. Tomás Gálvez P.

## Integrantes

| Nombre | Carné |
|---|---|
| Fernando Hernández | 23645 |
| Vianka Vanessa Castro Ordóñez | 23201 |
| Fernando Rueda | 23748 |

## Problema

**Bin Packing (1D):** dados _n_ objetos con tamaños positivos y una capacidad
de contenedor _C_, asignar cada objeto a un bin de capacidad _C_ minimizando
el número total de bins usados.

Es un problema NP-difícil clásico. Aquí se compara una solución exacta por
programación dinámica con bitmask (O(3ⁿ)) contra la heurística greedy
First Fit Decreasing (FFD) tanto teóricamente como empíricamente.

## Estructura del repositorio

```
proy2-ada/
├── docs/
│   ├── 01-descripcion.md             # Definición formal del problema
│   ├── 02-analisis-dp.md             # Subestructura óptima + recurrencia + pseudocódigo DP
│   ├── 03-greedy.md                  # Pseudocódigo FFD y ejemplo
│   ├── 04-complejidad.md             # Análisis de complejidad de ambos algoritmos
│   ├── 05-greedy-choice-property.md  # Discusión GCP y contraejemplo
│   └── 06-discusion-final.md         # Discusión final de aplicabilidad
├── src/
│   ├── dp_bitmask.py                 # DP exacta con bitmask
│   ├── greedy_ffd.py                 # Heurística FFD
│   ├── generator.py                  # Generador de instancias
│   └── benchmark.py                  # Runner del benchmark
├── tests/
│   ├── test_dp.py                    # Pruebas unitarias DP
│   └── test_greedy.py                # Pruebas unitarias FFD
├── data/
│   └── instancias.md                 # Listado tabulado de instancias
├── results/
│   ├── tiempos.csv                   # Tiempos medidos por el benchmark
│   ├── scatter.png                   # Diagrama de dispersión tiempo vs n
│   └── regresion.md                  # Regresión polinomial y ratios de calidad
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Instalación

Recomendado usar un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Cómo reproducir los resultados

### Correr los tests

```bash
pytest tests/
```

Deberían pasar las 20 pruebas (14 de DP + 6 de FFD).

### Listar las instancias generadas

```bash
python -c "import sys; sys.path.insert(0, 'src'); from generator import print_all_instances; print_all_instances()"
```

### Correr el benchmark completo

```bash
python src/benchmark.py
```

El benchmark mide ambos algoritmos sobre las 75 instancias y regenera:
- `results/tiempos.csv`
- `results/scatter.png`
- `results/regresion.md`

Tarda alrededor de 13–15 minutos por las corridas de DP con n = 20.

## Tabla resumen de hallazgos

| Aspecto | DP bitmask | FFD greedy |
|---|---|---|
| Complejidad teórica | O(3ⁿ) tiempo, O(2ⁿ) espacio | O(n²) tiempo, O(n) espacio |
| Tiempo a n = 5 | ~10 µs | ~1 µs |
| Tiempo a n = 20 | 85 – 150 s | ~7 µs |
| Base empírica del crecimiento | 2.94 (vs 3 teórico) | polinomial suave |
| Garantía de optimalidad | Sí | No |
| Ratio promedio FFD/OPT (75 instancias) | — | **1.0087** |
| Ratio máximo FFD/OPT | — | **1.25** |
| Cota teórica de FFD | — | (11/9)·OPT + 6/9 ≈ 1.222·OPT + 0.667 |

**Lectura corta:** la DP confirma su crecimiento exponencial empíricamente
(base ≈ 3). FFD es millones de veces más rápido a n = 20 y en la mayoría de
instancias aleatorias encuentra el óptimo; solo en instancias adversariales
construidas a propósito el ratio se acerca a la cota teórica.

## Entregables del proyecto

| Entregable | Dónde se cubre |
|---|---|
| 1. Descripción del problema | `docs/01-descripcion.md` |
| 2a. Subestructura óptima | `docs/02-analisis-dp.md` |
| 2b. Relación de recurrencia | `docs/02-analisis-dp.md` |
| 3a. Pseudocódigo DP | `docs/02-analisis-dp.md` |
| 3b. Pseudocódigo greedy | `docs/03-greedy.md` |
| 3c. Análisis de complejidad | `docs/04-complejidad.md` |
| 3d. Implementación funcional | `src/dp_bitmask.py`, `src/greedy_ffd.py` |
| 4. Discusión GCP | `docs/05-greedy-choice-property.md` |
| 5a. Listado de entradas | `data/instancias.md` (listado tabulado), `src/generator.py` (código que lo produce) |
| 5b. Diagrama de dispersión | `results/scatter.png` (generado por `src/benchmark.py`) |
| 5c. Regresión polinomial | `results/regresion.md` (generada por `src/benchmark.py`) |
| 6. Discusión final | `docs/06-discusion-final.md` |
| 7. Videos individuales | tabla más abajo |

## Videos individuales (entregable 7)

| Integrante | Enlace |
|---|---|
| Fernando Hernández (23645) | _pendiente_ |
| Vianka Castro (23201) | _pendiente_ |
| Fernando Rueda (23748) | _pendiente_ |
