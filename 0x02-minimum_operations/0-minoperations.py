#!/usr/bin/python3
""" Module for calculating Minimum Operations """


def minOperations(n):
    '''
        Calculate fewest number of operations required
        to paste n operations.
    '''
    # Step one is to factorize n
    factors = []
    i = 2

    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    # Step two is to add the factors
    total = sum(factors)
    # Step three is to return the sum of the factors
    return total
