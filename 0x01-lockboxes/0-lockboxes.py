#!/usr/bin/python3
'''
    ALX Interview - Lockboxes
'''


def canUnlockAll(boxes):
    '''
        Returns True if all the boxs can be unlocked
        and False if they can't
    '''
    keys = [0]
    opened_boxes = {0}

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                keys.append(key)

    return len(opened_boxes) == len(boxes)
