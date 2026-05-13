# Algoritmo Greedy: First Fit Decreasing

Para resolver el problema de Bin Packing con un enfoque greedy se utilizará la heurística **First Fit Decreasing (FFD)**.

La idea del algoritmo es ordenar primero los objetos de mayor a menor tamaño. Luego, cada objeto se coloca en el primer contenedor disponible donde todavía quepa. Si el objeto no cabe en ninguno de los contenedores abiertos, se crea un nuevo contenedor.

Este algoritmo no garantiza siempre la solución óptima, pero suele producir soluciones cercanas al óptimo con un tiempo de ejecución mucho menor que la programación dinámica exacta.

## Criterio greedy

El criterio greedy utilizado es:

> Colocar primero los objetos más grandes y asignar cada uno al primer bin donde quepa.

La razón de ordenar de mayor a menor es que los objetos grandes son más difíciles de acomodar. Si se dejan para el final, puede ser más probable que obliguen a abrir nuevos bins.

## Pseudocódigo

```text
FFD(items, capacity):
    ordenar items de mayor a menor
    bins = lista vacía

    para cada item en items:
        colocado = falso

        para cada bin en bins:
            si item cabe en bin:
                colocar item en bin
                colocado = verdadero
                detener búsqueda

        si colocado es falso:
            crear nuevo bin con item

    retornar cantidad de bins usados y asignación de objetos
```

## Ejemplo

Capacidad del bin:

```text
C = 10
```

Objetos:

```text
[4, 8, 1, 4, 2, 1]
```

Primero se ordenan de mayor a menor:

```text
[8, 4, 4, 2, 1, 1]
```

El algoritmo empieza con una lista vacía de contenedores.

### Paso 1

Se toma el objeto `8`.

Como no existe ningún contenedor abierto, se crea un nuevo bin:

```text
Bin 1: [8]
```

### Paso 2

Se toma el objeto `4`.

El `Bin 1` ya tiene peso `8`, entonces:

```text
8 + 4 = 12
```

Como `12 > 10`, el objeto no cabe en el `Bin 1`.

Se crea un nuevo bin:

```text
Bin 1: [8]
Bin 2: [4]
```

### Paso 3

Se toma el siguiente objeto `4`.

Se revisa el `Bin 1`:

```text
8 + 4 = 12
```

No cabe.

Se revisa el `Bin 2`:

```text
4 + 4 = 8
```

Sí cabe, entonces se coloca ahí:

```text
Bin 1: [8]
Bin 2: [4, 4]
```

### Paso 4

Se toma el objeto `2`.

Se revisa el `Bin 1`:

```text
8 + 2 = 10
```

Sí cabe, entonces se coloca ahí:

```text
Bin 1: [8, 2]
Bin 2: [4, 4]
```

### Paso 5

Se toma el objeto `1`.

Se revisa el `Bin 1`:

```text
8 + 2 + 1 = 11
```

No cabe.

Se revisa el `Bin 2`:

```text
4 + 4 + 1 = 9
```

Sí cabe, entonces se coloca ahí:

```text
Bin 1: [8, 2]
Bin 2: [4, 4, 1]
```

### Paso 6

Se toma el último objeto `1`.

Se revisa el `Bin 1`:

```text
8 + 2 + 1 = 11
```

No cabe.

Se revisa el `Bin 2`:

```text
4 + 4 + 1 + 1 = 10
```

Sí cabe, entonces se coloca ahí:

```text
Bin 1: [8, 2]
Bin 2: [4, 4, 1, 1]
```

## Resultado final

El algoritmo FFD utiliza:

```text
2 bins
```

Asignación final:

```text
Bin 1: [8, 2]
Bin 2: [4, 4, 1, 1]
```

En este caso, la solución greedy coincide con la solución óptima. Sin embargo, esto no siempre ocurre. FFD puede encontrar soluciones cercanas al óptimo, pero no garantiza obtener siempre la cantidad mínima de bins.

## Resultado esperado de la implementación

La función implementada debe retornar:

```text
cantidad de bins utilizados
asignación de objetos en cada bin
```

Por ejemplo:

```python
items = [4, 8, 1, 4, 2, 1]
capacity = 10

num_bins, bins = bin_packing_ffd(items, capacity)

print(num_bins)
print(bins)
```

Salida esperada:

```text
2
[[8, 2], [4, 4, 1, 1]]
```
