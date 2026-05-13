# Análisis de complejidad de DP y FFD

En este proyecto se comparan dos formas de resolver el problema de **Bin Packing**: una solución exacta con programación dinámica y una solución greedy usando la heurística **First Fit Decreasing (FFD)**.

La comparación se realiza principalmente en términos de **tiempo de ejecución**, **uso de memoria** y **calidad de la solución**.

---

## 1. Complejidad de la solución exacta con programación dinámica

La solución exacta utiliza programación dinámica con **bitmask**. Esto significa que cada subconjunto de objetos se representa mediante una máscara de bits.

Si hay `n` objetos, entonces existen:

```text
2^n
```

posibles subconjuntos de objetos.

Cada estado de la programación dinámica representaría un conjunto de objetos que aún deben ser empacados.

La recurrencia utilizada es:

```text
f(S) = min { 1 + f(S - T) }
```

en donde:

- `S` es el conjunto de objetos que todavía falta empacar.
- `T` es un subconjunto de `S` que cabe dentro de un bin.
- `S - T` representa los objetos restantes después de usar un bin para empacar `T`.
- `f(S)` representa la cantidad mínima de bins necesarios para empacar los objetos de `S`.

El caso base es:

```text
f(∅) = 0
```

Esto significa que si ya no quedan objetos por empacar, ya no se necesitan más bins.

---

## 2. Tiempo de ejecución de la programación dinámica

Para calcular la solución óptima, el algoritmo debe evaluar muchos subconjuntos posibles.

Primero, existen `2^n` estados posibles, porque cada estado representa un subconjunto distinto de objetos.

Además, para cada estado `S`, el algoritmo puede revisar varios subconjuntos `T` que podrían colocarse en un bin.

En el peor caso, esta revisión de subconjuntos produce una complejidad aproximada de:

```text
O(3^n)
```

Esta complejidad aparece porque, al analizar los subconjuntos, cada objeto puede encontrarse en una de tres situaciones:

1. No pertenece al conjunto `S`.
2. Pertenece a `S`, pero no se coloca en el subconjunto `T`.
3. Pertenece a `T`, es decir, se intenta colocar en el bin actual.

Por eso, aunque la programación dinámica evita repetir cálculos, sigue teniendo un crecimiento exponencial.

En conclusión, el tiempo de ejecución de la solución exacta es:

```text
O(3^n)
```

Esto significa que la solución exacta funciona bien para entradas pequeñas, pero se vuelve muy lenta cuando el número de objetos aumenta.

---

## 3. Espacio de la programación dinámica

La programación dinámica necesita guardar el resultado óptimo para cada subconjunto de objetos.

Como existen `2^n` subconjuntos posibles, el espacio requerido es:

```text
O(2^n)
```

Además, si se desea reconstruir la asignación final de objetos en bins, puede ser necesario guardar información adicional sobre qué subconjunto fue elegido en cada paso.

Por lo tanto, el espacio principal de la solución DP es:

```text
O(2^n)
```

---

## 4. Complejidad de First Fit Decreasing

La solución greedy utiliza la heurística **First Fit Decreasing**.

El algoritmo funciona de la siguiente manera:

1. Ordena los objetos de mayor a menor.
2. Toma cada objeto en ese orden.
3. Busca el primer bin donde el objeto quepa.
4. Si el objeto no cabe en ningún bin existente, abre un nuevo bin.

Este enfoque no revisa todas las combinaciones posibles. Por eso es mucho más rápido que la programación dinámica.

---

## 5. Tiempo de ejecución de FFD con implementación ingenua

Primero, el algoritmo ordena los `n` objetos de mayor a menor.

Ordenar los objetos tiene complejidad:

```text
O(n log n)
```

Después, el algoritmo recorre los objetos uno por uno.

Para cada objeto, revisa los bins existentes hasta encontrar el primero donde quepa.

En el peor caso, puede haber hasta `n` bins, por ejemplo cuando ningún objeto puede compartir bin con otro.

Entonces, para cada uno de los `n` objetos, se podrían revisar hasta `n` bins.

Esto produce:

```text
O(n^2)
```

Por lo tanto, la complejidad total de una implementación sencilla es:

```text
O(n log n + n^2)
```

Como `n^2` crece más rápido que `n log n`, se simplifica como:

```text
O(n^2)
```

---

## 6. Espacio de FFD

FFD necesita guardar los bins que se van creando.

En el peor caso, cada objeto podría necesitar su propio bin. Por eso, la cantidad máxima de bins es `n`.

El espacio requerido es:

```text
O(n)
```

También se puede necesitar una copia ordenada de la lista de objetos, lo cual mantiene el espacio en:

```text
O(n)
```

---

## 7. Posible mejora usando BBST

La implementación sencilla de FFD revisa los bins uno por uno. Por eso puede llegar a `O(n^2)`.

Sin embargo, se puede mejorar el manejo de los bins usando una estructura de datos más eficiente, como un **árbol binario balanceado** o **BBST** por sus siglas en inglés: *Balanced Binary Search Tree*.

La idea sería almacenar las capacidades restantes de los bins en una estructura ordenada, para buscar más rápido un bin donde el objeto pueda caber.

Con esta mejora, después de ordenar los objetos, cada búsqueda e inserción puede realizarse en aproximadamente:

```text
O(log n)
```

Como se procesan `n` objetos, la parte de asignación puede reducirse a:

```text
O(n log n)
```

Sumando el ordenamiento inicial, la complejidad mejorada sería:

```text
O(n log n)
```

Sin embargo, para este proyecto se utilizará la implementación sencilla con listas, ya que es más clara de entender, implementar y explicar.

Por eso, para el análisis empírico se tomará FFD como:

```text
O(n^2)
```

---

## 8. Comparación teórica de los algoritmos

| Algoritmo | Tipo de solución | Tiempo | Espacio | ¿Garantiza solución óptima? |
|---|---|---:|---:|---|
| Programación dinámica con bitmask | Exacta | `O(3^n)` | `O(2^n)` | Sí |
| First Fit Decreasing ingenuo | Greedy / heurística | `O(n^2)` | `O(n)` | No |
| First Fit Decreasing con BBST | Greedy / heurística optimizada | `O(n log n)` | `O(n)` | No |

---

## 9. Interpretación de la comparación

La programación dinámica sí tiene mejor calidad de solución porque encuentra el mínimo número posible de bins. Es decir, entrega la solución óptima.

Sin embargo, su costo computacional crece muy rápido. Esto limita su uso a entradas pequeñas, ya que para valores grandes de `n` el tiempo de ejecución puede volverse demasiado alto.

Por otro lado, First Fit Decreasing no garantiza siempre la solución óptima. Puede usar más bins que el mínimo real. Aun así, suele producir soluciones cercanas al óptimo y puede ejecutarse mucho más rápido.

Por esta razón, FFD es más práctico para entradas grandes, mientras que la programación dinámica es útil para obtener la solución óptima en casos pequeños y usarla como referencia para medir la calidad del greedy.

---

## 10. Conclusión

La diferencia principal entre ambos enfoques es que la programación dinámica explora combinaciones de objetos para asegurar una solución óptima, mientras que FFD toma decisiones locales rápidas.

Por eso, la programación dinámica tiene mayor precisión, pero peor tiempo de ejecución. En cambio, FFD tiene mejor rendimiento computacional, pero puede sacrificar calidad de solución.

En este proyecto, la solución DP servirá como referencia óptima para comparar qué tan buena es la solución greedy en diferentes entradas de prueba.
