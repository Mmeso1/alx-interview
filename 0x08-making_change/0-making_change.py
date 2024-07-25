#!/usr/bin/python3
""" ALX Interview Making Change
"""


def makeChange(coins, total):
    """
        Given a pile of coins of different values,
        determine the fewest number of coins needed
        to meet a given amount total
    """
    if total <= 0:
        return 0

    count = 0
    for coin in sorted(coins, reverse=True):
        while coin <= total:
            total -= coin
            count += 1

    if total == 0:
        return count
    else:
        return -1
