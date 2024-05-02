#!/usr/bin/python3
""" can box be opnened"""


def canUnlockAll(boxes):
    """can be opened or not"""
    p = 0
    unlocked_boxes = {}

    for i in boxes:
        if len(i) == 0 or p == 0:
            unlocked_boxes[p] = "always_unlocked"
        for k in i:
            if k < len(boxes) and k != p:
                unlocked_boxes[k] = k
        if len(unlocked_boxes) == len(boxes):
            return True
        p += 1
    return False
