import pytest
from src.greedy_ffd import bin_packing_ffd


def test_ffd_caso_basico():
    items = [4, 8, 1, 4, 2, 1]
    capacity = 10

    num_bins, bins = bin_packing_ffd(items, capacity)

    assert num_bins == 2
    assert all(sum(bin_actual) <= capacity for bin_actual in bins)


def test_ffd_objetos_exactos():
    items = [5, 5, 5, 5]
    capacity = 10

    num_bins, bins = bin_packing_ffd(items, capacity)

    assert num_bins == 2
    assert all(sum(bin_actual) <= capacity for bin_actual in bins)


def test_ffd_un_objeto_por_bin():
    items = [10, 10, 10]
    capacity = 10

    num_bins, bins = bin_packing_ffd(items, capacity)

    assert num_bins == 3
    assert all(sum(bin_actual) <= capacity for bin_actual in bins)


def test_ffd_lista_vacia():
    items = []
    capacity = 10

    num_bins, bins = bin_packing_ffd(items, capacity)

    assert num_bins == 0
    assert bins == []


def test_ffd_error_capacidad_invalida():
    with pytest.raises(ValueError):
        bin_packing_ffd([1, 2, 3], 0)


def test_ffd_error_item_mayor_que_capacidad():
    with pytest.raises(ValueError):
        bin_packing_ffd([2, 11], 10)