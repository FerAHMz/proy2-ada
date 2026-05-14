"""
Generador de instancias aleatorias para Bin Packing.

Cada instancia tiene un n (cantidad de objetos), una capacidad fija de bin,
una distribucion de tamanios y una semilla. La semilla hace que las
instancias sean reproducibles entre corridas, asi el benchmark da los
mismos resultados.
"""

import random
from dataclasses import dataclass


N_VALUES = [5, 8, 10, 12, 14, 16, 18, 20]
SEEDS = [1, 2, 3]
DISTRIBUTIONS = ["uniforme", "grandes", "pequenos"]
DEFAULT_CAPACITY = 20


@dataclass(frozen=True)
class Instance:
    id: str
    n: int
    capacity: int
    distribution: str
    seed: int
    items: tuple


def generate_items(n, capacity, distribution, seed):
    """Devuelve una lista de n tamanios segun la distribucion pedida."""
    rng = random.Random(seed)

    if distribution == "uniforme":
        lo, hi = 1, capacity
    elif distribution == "grandes":
        lo, hi = capacity // 2, capacity
    elif distribution == "pequenos":
        lo, hi = 1, max(1, capacity // 4)
    else:
        raise ValueError(f"Distribucion no reconocida: {distribution}")

    return [rng.randint(lo, hi) for _ in range(n)]


def make_instance(n, capacity, distribution, seed):
    items = generate_items(n, capacity, distribution, seed)
    instance_id = f"n{n:02d}-{distribution}-s{seed}"
    return Instance(instance_id, n, capacity, distribution, seed, tuple(items))


def all_instances(capacity=DEFAULT_CAPACITY):
    """Genera el set completo de instancias usado por el benchmark."""
    out = []
    for n in N_VALUES:
        for dist in DISTRIBUTIONS:
            for seed in SEEDS:
                out.append(make_instance(n, capacity, dist, seed))
    return out


def print_all_instances():
    """Imprime las instancias generadas para revisarlas a mano."""
    for inst in all_instances():
        print(f"{inst.id} | items={list(inst.items)}")
