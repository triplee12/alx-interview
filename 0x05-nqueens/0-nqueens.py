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

n = int(sys.argv[1])


def n_queens(m, i=0, a=[], b=[], c=[]):
    """
    Find possible positions.

    Args:
        m (int): number of queens
        i (int): interation
        a (list): list of numbers
        b (list): rows
        c (list): columns
    """
    if i < m:
        for j in range(m):
            if j not in a and i + j not in b and i - j not in c:
                yield from n_queens(m, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def check(m):
    """
    Check.

    Args:
        m (int): number of queens
    """
    k = []
    i = 0
    for solution in n_queens(m, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


check(n)
