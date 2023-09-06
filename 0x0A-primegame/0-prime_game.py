#!/usr/bin/python3
"""Prime game."""


def isWinner(x, nums):
    """
    Check who is the winner of the game.

    Args:
        x (int): The number of rounds.
        nums (list): aAn array of numbers.
    Returns:
        Name of the player that won the most rounds.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """Remove multiple of primes."""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
