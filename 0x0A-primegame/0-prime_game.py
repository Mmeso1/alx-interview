#!/usr/bin/python3
""" ALX Interview - Prime Game
"""


def is_prime(num):
    """ Calculates if a given number is a prime number
    """
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def filter_multiples(num, nums):
    """ Filters out a number and it's multiples from a list of numbers
    """
    # to_remove = []
    # for n in range(len(nums)):
    #     if nums[n] % num == 0:
    #         to_remove.append(nums[n])
    # for n in to_remove:
    #     nums.remove(n)
    # return nums
    return list(filter(lambda x: x % num != 0, nums))


def isWinner(x, nums):
    """ Plays the prime game between Ben and Mira and returns the winner
    """
    if x < 1 or not nums or x > 10000:
        return None

    scores = {"Maria": 0, "Ben": 0}
    for n in nums:
        numbers = list(range(1, n + 1))
        turn = "Maria"
        while True:
            primes = [i for i in numbers if is_prime(i)]
            if not primes:
                scores[turn] += 1
                break
            prime = min(primes)
            numbers = filter_multiples(prime, numbers)
            turn = "Ben" if turn == "Maria" else "Maria"

    if scores["Maria"] == scores["Ben"]:
        return None
    return "Maria" if scores["Maria"] > scores["Ben"] else "Ben"