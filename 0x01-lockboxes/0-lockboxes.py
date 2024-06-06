#!/usr/bin/python3
from queue import Queue
'''
    ALX Interview - Lockboxes
'''


def canUnlockAll(boxes):
    '''
        Returns True if all the boxs can be unlocked
        and False if they can't
    '''
    q = Queue()
    q.put(0)
    unlocked = set([0])

    while not q.empty():
        box = q.get()
        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                q.put(key)

    return len(unlocked) == len(boxes)
