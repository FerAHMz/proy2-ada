# 1. Descripción del Problema: Bin Packing (1D)

## Definición formal

**Entrada:**
- Un entero positivo _n_ (cantidad de objetos).
- Un vector de tamaños $S = (s_1, s_2, \ldots, s_n)$ donde $s_i \in \mathbb{Z}^+$ para todo $i$.
- Un entero positivo _C_ (capacidad de cada bin).

Se asume $s_i \leq C$ para todo $i$ (de lo contrario el problema no tiene solución).

**Salida:**  
Una asignación $f : \{1, \ldots, n\} \to \{1, \ldots, k\}$ tal que, para cada bin $b$:

$$\sum_{i : f(i) = b} s_i \leq C$$

**Función objetivo:**  
Minimizar $k$, el número de bins usados.

### Cota inferior trivial

Todo empaquetamiento óptimo usa al menos

$$k^* \geq \left\lceil \dfrac{\sum_{i=1}^{n} s_i}{C} \right\rceil$$

bins (cota de volumen). Esta cota puede no ser alcanzable.

## Ejemplo

Objetos con tamaños `[4, 7, 3, 6, 2, 5]` y capacidad `C = 10`:

| Bin | Objetos | Carga |
|-----|---------|-------|
| 1   | 7, 3    | 10    |
| 2   | 6, 4    | 10    |
| 3   | 5, 2    | 7     |

Solución óptima: **3 bins**.

## Variantes del problema

| Variante | Descripción |
|----------|-------------|
| **1D Bin Packing** (clásico) | Objetos con un tamaño escalar; bins con capacidad escalar C. |
| **2D / 3D Bin Packing** | Objetos rectangulares/cúbicos; bins de área/volumen fijo. Sin rotación ni solapamiento. |
| **Online Bin Packing** | Los objetos llegan uno a uno y deben asignarse antes de conocer los siguientes. |
| **Variable-sized Bin Packing** | Se dispone de bins de distintas capacidades con costos diferentes. |
| **Bin Packing fraccional** | Se permite partir objetos; tiene solución polinomial por flujo. |

## Complejidad y NP-dificultad

El problema de decisión asociado — ¿existe empaquetamiento en a lo sumo _k_ bins? — es
**NP-completo**. La demostración clásica es por reducción desde **3-PARTITION** (Garey & Johnson, 1979):

- Dado un multiconjunto $A = \{a_1, \ldots, a_{3m}\}$ con $\sum a_i = m \cdot B$ y
  $B/4 < a_i < B/2$ para todo $i$, se pregunta si $A$ puede partirse en $m$ triples de suma $B$.
- Se construye una instancia de Bin Packing con capacidad $C = B$ y $n = 3m$ objetos de
  tamaños $a_i$.
- Hay un empaquetamiento en $m$ bins si y sólo si existe una 3-partición válida.

Como el problema de optimización (minimizar _k_) es al menos tan difícil como el de decisión,
es **NP-difícil**. Ningún algoritmo polinomial exacto es conocido salvo que P = NP.

## Justificación de elección

El Bin Packing satisface todos los requisitos del proyecto:

1. **Solución DP superpolinomial existente:** la formulación con bitmask tiene complejidad
   O(3ⁿ) en tiempo y O(2ⁿ) en espacio.
2. **Algoritmo greedy natural:** First-Fit Decreasing (FFD) es eficiente (O(n log n)) y tiene
   cota de aproximación demostrable: $\text{FFD}(I) \leq \tfrac{11}{9}\,\text{OPT}(I) + \tfrac{6}{9}$.
3. **Interés práctico:** aparece en scheduling de tareas en procesadores, carga de camiones,
   corte de tela/madera, asignación de páginas en memoria virtual, y empaquetado físico.
4. **No fue visto en clase:** cumple la restricción del enunciado.

## Referencias

- Garey, M. R., & Johnson, D. S. (1979). *Computers and Intractability: A Guide to the Theory
  of NP-Completeness*. W. H. Freeman.
- Coffman, E. G., Garey, M. R., & Johnson, D. S. (1984). Approximation Algorithms for Bin
  Packing: A Survey. *Design and Analysis of Approximation Algorithms*.
- Korf, R. E. (2002). A new algorithm for optimal bin packing. *AAAI/IAAI*, 731–736.
