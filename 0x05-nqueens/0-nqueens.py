#!/usr/bin/python3
"""N queens."""

import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n: int = int(sys.argv[1])


def n_queens(n: int, i: int = 0, a: list = [], b: list = [], c: list = []):
    """
    Find possible positions.

    Args:
        n (int): number of queens
        i (int): interation
        a (list): list of numbers
        b (list): rows
        c (list): columns
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from n_queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def check(n: int):
    """
    Check.

    Args:
        n (int): number of queens
    """
    k: list = []
    i = 0
    for solution in n_queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


check(n)
