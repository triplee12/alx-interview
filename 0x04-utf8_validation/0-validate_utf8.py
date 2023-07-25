#!/usr/bin/python3
"""UTF-8 string representation."""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Utf8 string representation.

    Args:
        data (List[int]): list of integers to convert

    Returns:
        bool: True if the string is valid UTF string, otherwise False
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
