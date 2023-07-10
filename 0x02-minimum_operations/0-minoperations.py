#!/usr/bin/python3
"""Minimum operations."""

import math


def minOperations(n) -> int:
    """
    Minimum operations.

    Args:
        n (int): Number of operations
    Returns:
        int: Number of operations
    """
    if n == 1:
        return 0

    # Find factors of n
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 1:
        factors.append(n)

    # Calculate the minimum number of operations
    min_ops: int = sum(factors)
    return min_ops
