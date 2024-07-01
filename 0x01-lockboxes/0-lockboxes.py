#!/usr/bin/python3
""" LockBoxes """


def canUnlockAll(boxes):
    """ Determines if al boxes can be opened """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
