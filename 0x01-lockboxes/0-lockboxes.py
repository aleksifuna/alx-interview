#!/usr/bin/python3
"""Supplies a function canUnlockAll"""

def canUnlockAll(boxes):
    """checks if all lockboxes can be unlocked"""
    keys = [0]
    i = 0

    while True:
        if i >= len(keys):
            break
        idx =keys[i]
        for item in boxes[idx]:
            if item < len(boxes) and item not in keys:
                keys.append(item)
        i += 1
    if len(keys) == len(boxes):
        return True
    return False
