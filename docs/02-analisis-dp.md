# 2. Análisis del Problema: Subestructura Óptima y DP con Bitmask

## 2a. Demostración de subestructura óptima

### Planteamiento

Afirmamos que **Bin Packing presenta subestructura óptima**: toda solución óptima para un
conjunto de objetos $S$ contiene necesariamente soluciones óptimas para los subconjuntos
que llenan cada bin.

### Argumento de corte y pegado (Cut-and-Paste)

Sea $\text{OPT}(S)$ el número mínimo de bins para empaquetar todos los objetos del conjunto $S$,
con capacidad $C$.

**Notación:** Representamos cada subconjunto de objetos como una máscara de bits $M \subseteq \{1,\ldots,n\}$.

**Paso 1 — Estructura de la solución óptima.**  
Sea $\mathcal{B}^* = (B_1^*, B_2^*, \ldots, B_k^*)$ una solución óptima para $S$ (con $k = \text{OPT}(S)$).
Sin pérdida de generalidad, el bin $B_1^*$ contiene cierto subconjunto de objetos $T \subseteq S$
con $\sum_{i \in T} s_i \leq C$.

El resto de los objetos, $S' = S \setminus T$, son empaquetados en los bins $B_2^*, \ldots, B_k^*$,
usando $k - 1$ bins.

**Paso 2 — Hipótesis de contradicción.**  
Supongamos que $(B_2^*, \ldots, B_k^*)$ **no es óptimo** para $S'$, es decir, existe otra
asignación $\mathcal{B}'$ que empaqueta $S'$ en $k' < k-1$ bins.

**Paso 3 — Construcción de solución mejor.**  
Tomamos la solución $\mathcal{B}'' = (\{T\}) \cup \mathcal{B}'$:
- El bin que contiene $T$ sigue siendo válido ($\sum_{i \in T} s_i \leq C$).
- Los $k'$ bins de $\mathcal{B}'$ empaquetan $S'$.
- Total de bins usados: $1 + k' < 1 + (k-1) = k$.

Esto contradice que $\mathcal{B}^*$ es óptimo para $S$. $\square$

**Conclusión:** si $\mathcal{B}^*$ es óptima para $S$, entonces la sub-solución inducida sobre
cualquier $S' = S \setminus T$ (donde $T$ ocupa el primer bin) también es óptima para $S'$.
El problema tiene **subestructura óptima**.

### Decisión y subproblema residual

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuál es la decisión principal? | Elegir el subconjunto $T \subseteq S$ que llenará el próximo bin. |
| ¿Qué subproblema queda? | Empaquetar $S' = S \setminus T$ con el menor número de bins posible. |
| ¿Qué pasa si el subproblema no es óptimo? | Se puede construir una solución mejor para $S$ (contradicción con optimalidad). |
| ¿Cómo se combina? | $\text{OPT}(S) = 1 + \text{OPT}(S \setminus T^*)$ donde $T^*$ es el subconjunto elegido. |

---

## 2b. Relación de recurrencia

### Representación con bitmask

Codificamos el conjunto de objetos aún sin empaquetar como un entero de $n$ bits.
El bit $i$ (posición $i$, con $0 \leq i < n$) vale 1 si el objeto $i$ no ha sido asignado.

- **Estado:** $f(M)$ = número mínimo de bins para empaquetar exactamente los objetos
  indicados por la máscara $M$.
- **Dominio:** $M \in \{0, 1, 2, \ldots, 2^n - 1\}$.

### Precómputo: subconjuntos válidos

Definimos el conjunto de **máscaras factibles** (subconjuntos que caben en un solo bin):

$$\text{fits} = \{ T \subseteq \{0,\ldots,n-1\} \mid \sum_{i \in T} s_i \leq C,\ T \neq \emptyset \}$$

Este conjunto se puede precalcular en $O(2^n \cdot n)$ revisando todos los subconjuntos.

### Caso base

$$f(\emptyset) = f(0) = 0$$

No quedan objetos, no se necesita ningún bin.

### Transición (recurrencia principal)

Para cualquier máscara $M \neq \emptyset$:

$$f(M) = \min_{\substack{T \subseteq M \\ T \in \text{fits}}} \bigl(1 + f(M \setminus T)\bigr)$$

donde $M \setminus T$ en aritmética de bits es $M\ \mathtt{XOR}\ (M\ \mathtt{AND}\ T) = M \oplus T$
(ya que $T \subseteq M$ garantiza que los bits de $T$ son un subconjunto de los de $M$).

### Valor óptimo

$$\text{OPT}(s_1, \ldots, s_n, C) = f\bigl(2^n - 1\bigr)$$

La máscara $2^n - 1$ tiene todos los $n$ bits activos, representando que todos los objetos
deben ser asignados.

### Resumen de la DP

| Componente | Definición |
|---|---|
| **Estado** | $f(M)$: bins mínimos para empaquetar los objetos en máscara $M$ |
| **Caso base** | $f(0) = 0$ |
| **Transición** | $f(M) = \min_{T \subseteq M,\ T \in \text{fits}} (1 + f(M \oplus T))$ |
| **Respuesta** | $f(2^n - 1)$ |
| **# estados** | $2^n$ |
| **Transiciones por estado** | Hasta $2^n$ (todos los subconjuntos de $M$) |

---

## 3a. Pseudocódigo DP con Bitmask

```
BIN-PACKING-DP(s[0..n-1], C):
    // Precalcular qué subconjuntos no vacíos caben en un bin
    fits ← lista vacía
    for mask ← 1 to 2^n - 1 do
        total ← sum of s[i] for each i where bit i of mask is 1
        if total ≤ C then
            fits.append(mask)

    // Inicializar tabla DP
    dp[0] ← 0
    for mask ← 1 to 2^n - 1 do
        dp[mask] ← ∞

    // Llenar tabla DP en orden creciente de máscara
    for mask ← 1 to 2^n - 1 do
        // Enumerar todos los subconjuntos de mask que están en fits
        sub ← mask
        while sub > 0 do
            if sub ∈ fits then
                val ← 1 + dp[mask XOR sub]
                if val < dp[mask] then
                    dp[mask] ← val
            sub ← (sub - 1) AND mask   // siguiente subconjunto de mask

    return dp[2^n - 1]
```

**Truco de enumeración de subconjuntos:** el lazo `sub = (sub - 1) AND mask` itera
eficientemente sobre todos los subconjuntos no vacíos de `mask` en tiempo proporcional
al número de subconjuntos, sin iterar sobre todas las máscaras.

### Reconstrucción de la asignación

```
RECONSTRUCT(s[0..n-1], C, dp, parent):
    // parent[mask] = subconjunto T elegido para el primer bin de mask
    mask ← 2^n - 1
    bins ← lista vacía
    while mask ≠ 0 do
        T ← parent[mask]
        bin_content ← {i : bit i de T es 1}
        bins.append(bin_content)
        mask ← mask XOR T
    return bins
```

---

## Análisis de complejidad de la DP

### Tiempo

El costo dominante es la doble enumeración: para cada máscara $M$, enumerar todos sus
subconjuntos $T \subseteq M$.

El total de pares $(M, T)$ con $T \subseteq M$ es:

$$\sum_{M=0}^{2^n-1} 2^{|M|} = \sum_{k=0}^{n} \binom{n}{k} 2^k = 3^n$$

(por el teorema binomial con $(1+2)^n = 3^n$).

Por lo tanto, el tiempo de ejecución es $\Theta(3^n)$, que es **superpolinomial** en $n$.

Para $n = 20$: $3^{20} \approx 3.5 \times 10^9$ operaciones — inviable en la práctica.  
Para $n = 15$: $3^{15} \approx 14$ millones — manejable en segundos.

### Espacio

La tabla `dp` almacena un valor por cada subconjunto: $O(2^n)$.  
El arreglo de precómputo `fits` también es $O(2^n)$ en el peor caso.

**Espacio total:** $O(2^n)$.

### Comparación con fuerza bruta

| Método | Tiempo | Espacio |
|--------|--------|---------|
| Fuerza bruta (todas las asignaciones) | $O(n^n)$ | $O(n)$ |
| DP con bitmask | $O(3^n)$ | $O(2^n)$ |
| FFD (greedy) | $O(n^2)$ | $O(n)$ |

La DP reduce exponencialmente el espacio de búsqueda respecto a la fuerza bruta, pero sigue
siendo exponencial. El greedy FFD es el único con tiempo polinomial, a costa de perder optimalidad.
