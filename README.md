# Proyecto #2 — Bin Packing Problem

**CC3894 – Análisis y Diseño de Algoritmos**  
Universidad del Valle de Guatemala · Semestre 1, 2026  
Docente: Ing. Tomás Gálvez P.

## Integrantes

| Nombre | Carné |
|---|---|
| Fernando Hernández | 23645 |
| Vianka Vanessa Castro Ordoñez | 23201 |
| Fernando Rueda | 23748 |

## Problema

**Bin Packing (1D):** dados _n_ objetos con tamaños positivos y una capacidad de contenedor _C_,
asignar cada objeto a un bin de capacidad _C_ minimizando el número total de bins usados.

Es un problema NP-difícil clásico que admite solución exacta mediante programación dinámica
(con bitmask, O(3ⁿ)) y una buena aproximación greedy con First-Fit Decreasing (FFD).

## Estructura del repositorio

```
proy2-ada/
├── docs/
│   ├── 01-descripcion.md        # Definición formal del problema
│   ├── 02-analisis-dp.md        # Subestructura óptima + recurrencia + pseudocódigo DP
│   ├── 03-greedy.md             # Pseudocódigo FFD y análisis
│   ├── 04-complejidad.md        # Análisis de complejidad de ambos algoritmos
│   ├── 05-greedy-choice-property.md  # Discusión GCP y contraejemplo
│   └── 06-discusion-final.md    # Discusión final de aplicabilidad
├── src/
│   ├── dp_bitmask.py            # DP exacta con bitmask
│   └── greedy_ffd.py            # Heurística FFD
├── tests/
│   ├── test_dp.py               # Pruebas unitarias DP
│   └── test_greedy.py           # Pruebas unitarias FFD
├── data/
│   └── instancias.md            # Listado tabulado de instancias de prueba
├── results/
│   ├── tiempos.csv              # Tiempos medidos (generado por benchmark)
│   ├── scatter.png              # Diagrama de dispersión (generado)
│   └── regresion.md             # Regresión polinomial y análisis
├── src/
│   ├── generator.py             # Generador de instancias aleatorias
│   └── benchmark.py             # Runner de benchmark
├── requirements.txt
└── README.md
```

## Instalación y uso

```bash
pip install -r requirements.txt

# Ejecutar tests
pytest tests/

# Correr benchmark completo (genera CSV y gráficas)
python src/benchmark.py
```

## Videos individuales

| Integrante | Enlace |
|---|---|
| Fernando Hernández (23645) | _pendiente_ |
| Vianka Castro (23201) | _pendiente_ |
| Fernando Rueda (23748) | _pendiente_ |
