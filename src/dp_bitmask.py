"""
Exact Bin Packing solver using bitmask dynamic programming.

Complexity: O(3^n) time, O(2^n) space.
Practical limit: n <= 20 (n <= 15 recommended for sub-second runtimes).
"""

from __future__ import annotations


def bin_packing_dp(items: list[int], capacity: int) -> tuple[int, list[list[int]]]:
    """Return the minimum number of bins and a valid assignment.

    Args:
        items: list of item sizes (positive integers, each <= capacity).
        capacity: bin capacity (positive integer).

    Returns:
        (num_bins, assignment) where assignment is a list of bins, each bin
        being a list of 0-based item indices assigned to it.

    Raises:
        ValueError: if any item size exceeds capacity.
    """
    n = len(items)
    if n == 0:
        return 0, []

    for i, s in enumerate(items):
        if s > capacity:
            raise ValueError(f"Item {i} has size {s} > capacity {capacity}")

    total_masks = 1 << n  # 2^n

    # Precompute sum of each subset using the inclusion relation:
    # sum[mask | (1<<i)] = sum[mask] + items[i]
    subset_sum = [0] * total_masks
    for mask in range(1, total_masks):
        lsb = mask & (-mask)          # lowest set bit as a power of two
        i = lsb.bit_length() - 1     # index of that bit
        subset_sum[mask] = subset_sum[mask ^ lsb] + items[i]

    # Collect all non-empty subsets that fit in a single bin
    fits = [m for m in range(1, total_masks) if subset_sum[m] <= capacity]

    # DP table: dp[mask] = min bins to pack exactly the items in mask
    INF = n + 1
    dp = [INF] * total_masks
    dp[0] = 0

    # parent[mask] = the subset chosen as the "first bin" for mask
    parent = [0] * total_masks

    full = total_masks - 1  # all bits set

    for mask in range(1, total_masks):
        # Iterate over all subsets of mask that fit in one bin
        sub = mask
        while sub:
            if subset_sum[sub] <= capacity:
                remainder = mask ^ sub
                val = 1 + dp[remainder]
                if val < dp[mask]:
                    dp[mask] = val
                    parent[mask] = sub
            sub = (sub - 1) & mask  # next subset of mask

    # Reconstruct assignment
    assignment: list[list[int]] = []
    mask = full
    while mask:
        t = parent[mask]
        bin_items = [i for i in range(n) if (t >> i) & 1]
        assignment.append(bin_items)
        mask ^= t

    return dp[full], assignment
