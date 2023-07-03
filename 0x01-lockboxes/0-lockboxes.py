#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    Lockboxes

    Args:
        boxes (list): list of integer lists
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
