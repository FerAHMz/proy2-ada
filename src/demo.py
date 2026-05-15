"""
Demo visual de Bin Packing: DP exacta vs FFD greedy.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from dp_bitmask import bin_packing_dp
from greedy_ffd import bin_packing_ffd


BAR_WIDTH = 20  # caracteres que representa la capacidad total


def barra(suma, capacity):
    llenos = round(BAR_WIDTH * suma / capacity)
    vacios = BAR_WIDTH - llenos
    return "█" * llenos + "░" * vacios


def mostrar_resultado(titulo, num_bins, assignment, items, capacity, es_dp=True):
    print(f"\n── {titulo} {'─' * max(0, 54 - len(titulo))}")
    print(f"  Bins usados: {num_bins}\n")

    if es_dp:
        # assignment de DP contiene índices
        for idx, bin_indices in enumerate(assignment, 1):
            sizes = [items[i] for i in bin_indices]
            suma = sum(sizes)
            print(f"  Bin {idx} │{barra(suma, capacity)}│  {sizes}  suma={suma}/{capacity}")
    else:
        # assignment de FFD contiene tamaños directamente
        for idx, bin_sizes in enumerate(assignment, 1):
            suma = sum(bin_sizes)
            print(f"  Bin {idx} │{barra(suma, capacity)}│  {bin_sizes}  suma={suma}/{capacity}")


def ejecutar_caso(items, capacity, titulo):
    sep = "=" * 62
    print(f"\n{sep}")
    print(f"  {titulo}")
    print(f"  Objetos: {items}   C = {capacity}")
    print(sep)

    dp_bins, dp_asgn = bin_packing_dp(list(items), capacity)
    mostrar_resultado("PROGRAMACIÓN DINÁMICA — exacta O(3ⁿ)", dp_bins, dp_asgn, items, capacity, es_dp=True)

    ffd_bins, ffd_asgn = bin_packing_ffd(list(items), capacity)
    mostrar_resultado("GREEDY First Fit Decreasing — O(n²)", ffd_bins, ffd_asgn, items, capacity, es_dp=False)

    ratio = ffd_bins / dp_bins if dp_bins > 0 else 1.0
    print()
    if ffd_bins == dp_bins:
        print(f"  Ratio FFD/OPT = {ratio:.3f}  ✓  greedy encontró el óptimo")
    else:
        print(f"  Ratio FFD/OPT = {ratio:.3f}  ✗  greedy usó {ffd_bins - dp_bins} bin(s) extra")
    print(sep)


def main():
    print("\n" + "=" * 62)
    print("  DEMO — Bin Packing: Programación Dinámica vs Greedy FFD")
    print("=" * 62)

    # Caso 1: ejemplo del enunciado — ambos encuentran el óptimo
    ejecutar_caso(
        items=[4, 7, 3, 6, 2, 5],
        capacity=10,
        titulo="CASO 1 — Ejemplo del enunciado"
    )

    # Caso 2: contraejemplo greedy choice property — FFD falla
    ejecutar_caso(
        items=[6, 5, 3, 2, 2, 2],
        capacity=10,
        titulo="CASO 2 — Contraejemplo: greedy choice property"
    )

    # Caso 3: todos del mismo tamaño con sobrante
    ejecutar_caso(
        items=[3, 3, 3, 3, 3],
        capacity=10,
        titulo="CASO 3 — Objetos iguales con espacio sobrante"
    )


main()
