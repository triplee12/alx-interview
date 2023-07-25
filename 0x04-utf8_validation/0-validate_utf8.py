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
    # valid = "".join([chr(x) for x in data]).encode("utf-8")
    # if valid.decode("utf-8"):
    #     print(valid)
    #     return True
    # print(valid)
    # return False
    valid = []
    for i in data:
        if i >= 256:
            valid.append(False)
        valid.append(True)
    if False in valid:
        return False
    return True
