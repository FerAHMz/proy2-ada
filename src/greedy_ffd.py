"""
Heurística First Fit Decreasing (FFD) para el problema Bin Packing.

Lo que realiza este algoritmo es que ordena los objetos de mayor a menor 
y luego coloca cada objeto en el primer bin donde quepa. 

Si no cabe en ningún bin existente, abre uno nuevo.
"""


def bin_packing_ffd(items, capacity):
    """
    Resuelve Bin Packing usando la heurística First Fit Decreasing.

    Args:
        items (list[int | float]): tamaños de los objetos.
        capacity (int | float): capacidad máxima de cada bin.

    Returns:
        tuple[int, list[list[int | float]]]: cantidad de bins usados y asignación.
    """
    if capacity <= 0:
        raise ValueError("La capacidad debe ser mayor que 0.")

    if any(item <= 0 for item in items):
        raise ValueError("Todos los objetos deben tener tamaño positivo.")

    if any(item > capacity for item in items):
        raise ValueError("No se puede empacar un objeto mayor que la capacidad del bin.")

    sorted_items = sorted(items, reverse=True)

    bins = []

    for item in sorted_items:
        placed = False

        for bin_actual in bins:
            if sum(bin_actual) + item <= capacity:
                bin_actual.append(item)
                placed = True
                break

        if not placed:
            bins.append([item])

    return len(bins), bins