"""
Unit tests for dp_bitmask.bin_packing_dp.

All expected optimal values are verified by hand or by exhaustive enumeration
for small n, so these tests act as a correctness oracle.
"""

import pytest

from dp_bitmask import bin_packing_dp


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def assignment_is_valid(items, capacity, assignment, expected_bins):
    """Return True iff the assignment respects all constraints."""
    n = len(items)
    covered = set()
    for bin_items in assignment:
        assert sum(items[i] for i in bin_items) <= capacity, "Bin overflows"
        for i in bin_items:
            assert i not in covered, f"Item {i} assigned twice"
            covered.add(i)
    assert covered == set(range(n)), "Not all items assigned"
    assert len(assignment) == expected_bins, (
        f"Expected {expected_bins} bins, got {len(assignment)}"
    )
    return True


# ---------------------------------------------------------------------------
# Basic cases
# ---------------------------------------------------------------------------

def test_empty_input():
    k, asgn = bin_packing_dp([], 10)
    assert k == 0
    assert asgn == []


def test_single_item():
    k, asgn = bin_packing_dp([5], 10)
    assert k == 1
    assert assignment_is_valid([5], 10, asgn, 1)


def test_two_items_fit_in_one_bin():
    items = [4, 6]
    k, asgn = bin_packing_dp(items, 10)
    assert k == 1
    assert assignment_is_valid(items, 10, asgn, 1)


def test_two_items_need_two_bins():
    items = [6, 7]
    k, asgn = bin_packing_dp(items, 10)
    assert k == 2
    assert assignment_is_valid(items, 10, asgn, 2)


# ---------------------------------------------------------------------------
# Known optimal solutions (n <= 6, verified by hand)
# ---------------------------------------------------------------------------

def test_three_items_two_bins():
    # [4, 7, 3], C=10 -> bins {7,3} and {4}: 2 bins
    items = [4, 7, 3]
    k, asgn = bin_packing_dp(items, 10)
    assert k == 2
    assert assignment_is_valid(items, 10, asgn, 2)


def test_example_from_description():
    # [4, 7, 3, 6, 2, 5], C=10 -> optimal is 3 bins
    items = [4, 7, 3, 6, 2, 5]
    k, asgn = bin_packing_dp(items, 10)
    assert k == 3
    assert assignment_is_valid(items, 10, asgn, 3)


def test_all_items_same_size_exact_fill():
    # 6 items of size 5, C=10 -> 3 bins
    items = [5] * 6
    k, asgn = bin_packing_dp(items, 10)
    assert k == 3
    assert assignment_is_valid(items, 10, asgn, 3)


def test_all_items_same_size_with_remainder():
    # 5 items of size 3, C=10 -> ceil(15/10) = 2 bins: {3,3,3} and {3,3} -> 2
    items = [3] * 5
    k, asgn = bin_packing_dp(items, 10)
    assert k == 2
    assert assignment_is_valid(items, 10, asgn, 2)


def test_each_item_fills_one_bin():
    # 4 items of size 10, C=10 -> 4 bins
    items = [10] * 4
    k, asgn = bin_packing_dp(items, 10)
    assert k == 4
    assert assignment_is_valid(items, 10, asgn, 4)


def test_tight_packing():
    # [2, 3, 4, 5, 6, 7], C=10
    # Optimal: {7,3}, {6,4}, {5,2} -> 3 bins
    items = [2, 3, 4, 5, 6, 7]
    k, asgn = bin_packing_dp(items, 10)
    assert k == 3
    assert assignment_is_valid(items, 10, asgn, 3)


def test_worst_case_n6():
    # [1,2,3,4,5,6], C=7
    # Optimal: {6,1}, {5,2}, {4,3} -> 3 bins
    items = [1, 2, 3, 4, 5, 6]
    k, asgn = bin_packing_dp(items, 7)
    assert k == 3
    assert assignment_is_valid(items, 7, asgn, 3)


def test_single_item_equal_to_capacity():
    items = [10]
    k, asgn = bin_packing_dp(items, 10)
    assert k == 1
    assert assignment_is_valid(items, 10, asgn, 1)


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def test_item_exceeds_capacity_raises():
    with pytest.raises(ValueError):
        bin_packing_dp([5, 11, 3], 10)


# ---------------------------------------------------------------------------
# Consistency: num_bins matches len(assignment)
# ---------------------------------------------------------------------------

def test_return_count_matches_assignment_length():
    items = [3, 5, 2, 8, 1, 6]
    k, asgn = bin_packing_dp(items, 10)
    assert k == len(asgn)
    assert assignment_is_valid(items, 10, asgn, k)
