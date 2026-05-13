# Discusión sobre Greedy Choice Property en Bin Packing

## 1. ¿Qué es la greedy choice property?

La **greedy choice property** es una propiedad que tienen algunos problemas de optimización donde una decisión localmente óptima puede formar parte de una solución globalmente óptima.

En otras palabras, si un problema cumple esta propiedad, se puede construir una solución óptima tomando decisiones greedy paso a paso, sin necesidad de revisar todas las combinaciones posibles.

En este proyecto, esta discusión es importante porque se está comparando una solución exacta con programación dinámica contra una heurística greedy.

---

## 2. Aplicación al problema de Bin Packing

En el problema de **Bin Packing**, se tiene un conjunto de objetos con distintos tamaños y una cantidad ilimitada de contenedores con una misma capacidad máxima.

El objetivo es minimizar la cantidad de contenedores utilizados, sin exceder la capacidad de ninguno.

La heurística utilizada en este proyecto es **First Fit Decreasing (FFD)**. Este algoritmo sigue el siguiente criterio greedy:

1. Ordenar los objetos de mayor a menor.
2. Tomar cada objeto en ese orden.
3. Colocarlo en el primer bin donde quepa.
4. Si no cabe en ningún bin abierto, crear un nuevo bin.

Este criterio es razonable porque intenta acomodar primero los objetos más grandes, ya que suelen ser los más difíciles de colocar. Sin embargo, esto no garantiza que la solución final sea óptima.

---

## 3. ¿Bin Packing cumple la greedy choice property?

Bin Packing **no cumple la greedy choice property de forma general**.

La razón es que una decisión que parece buena en el momento puede limitar las combinaciones futuras. Al colocar un objeto en el primer bin disponible, el algoritmo puede usar espacio que después hubiera sido necesario para lograr una mejor distribución.

Por eso, una solución greedy puede terminar usando más bins que la solución óptima.

---

## 4. Por Contraejemplo

Considere la siguiente instancia:

```text
Capacidad de cada bin: 10

Objetos:
[6, 5, 3, 2, 2, 2]
```

Los objetos ya están ordenados de mayor a menor, por lo que First Fit Decreasing los procesa en este orden:

```text
[6, 5, 3, 2, 2, 2]
```

Aplicando FFD:

```text
Bin 1: [6, 3]
Bin 2: [5, 2, 2]
Bin 3: [2]
```

FFD utiliza:

```text
3 bins
```

Sin embargo, existe una mejor asignación:

```text
Bin 1: [6, 2, 2]
Bin 2: [5, 3, 2]
```

Esta solución utiliza:

```text
2 bins
```

Por lo tanto, este ejemplo muestra que la decisión greedy de colocar cada objeto en el primer bin donde quepa no siempre conduce a la solución óptima.

---

## 5. Por qué no se puede garantizar optimalidad greedy

Para demostrar que un algoritmo greedy es óptimo, normalmente se necesita probar que cada elección local puede formar parte de alguna solución óptima.

En Bin Packing esto no se puede garantizar.

Cuando se coloca un objeto en un bin, esa decisión afecta el espacio disponible para todos los objetos restantes. Por eso, el orden y la combinación de objetos tienen un impacto fuerte en la solución final.

FFD no evalúa todas las formas posibles de agrupar objetos. Únicamente toma la primera opción válida según el orden de los bins existentes.

---

## 6. Relación con matroides

Algunos problemas greedy pueden justificarse mediante una estructura de **matroide ponderada**. En esos casos, la estructura del problema permite seleccionar elementos de forma greedy y aun así garantizar optimalidad.

Bin Packing no se modela naturalmente como una matroide ponderada para este objetivo, porque las decisiones de asignación no son independientes entre sí.

Colocar un objeto en un bin modifica la capacidad restante y cambia las posibilidades para los demás objetos. Por lo tanto, no existe una estructura de independencia simple que permita justificar la optimalidad de FFD mediante matroides.

---

## 7. Calidad de la solución greedy

Aunque First Fit Decreasing no garantiza siempre la solución óptima, sí es una heurística conocida por producir soluciones cercanas al óptimo en muchos casos prácticos.

Una cota teórica conocida para FFD es:

```text
FFD ≤ (11/9)OPT + 6/9
```

Esto significa que la cantidad de bins usados por FFD está acotada respecto a la solución óptima. Aunque no siempre encuentra el óptimo, suele producir resultados razonablemente buenos con un tiempo de ejecución mucho menor que la programación dinámica.

---

## 8. Conclusión

Bin Packing no cumple la greedy choice property de forma general.

La heurística First Fit Decreasing toma decisiones rápidas y prácticas, pero no puede garantizar que cada decisión local pertenezca a una solución óptima global.

Por esta razón, FFD es útil cuando se busca una solución rápida y cercana al óptimo, mientras que la programación dinámica es más adecuada cuando se necesita garantizar la solución óptima en instancias pequeñas.
