#!/usr/bin/env python3

from typing import Iterable, Set
import numpy as np


##### Python Reminder

# Fix

def fix_me(numbers: Iterable[int]) -> Iterable[int]:
    # Return all the even numbers in the parameter numbers.
    results = list()
    for num in numbers:
        if num % 2 == 0:
            results.append(num)
    return results


def fix_me_too(numbers: Iterable[int], threshold: int) -> int:
    """
    The function takes an iterable of integers and a threshold.
    The function returns the number of values in numbers that are above the given threshold.
    """
    count = 0
    for n in numbers:
        if n > threshold:
            count += 1
        return count


# Implement

def get_shared_items(sets: Iterable[Set[int]]) -> Set[int]:
    # Return the set of numbers that are shared by all sets
    dictionary = dict()
    count = 0
    for s in sets:
        count += 1
        for i in s:
            if i in dictionary:
                dictionary.update({i: 1})
                continue
            dictionary.update({i: dictionary[i] + 1})
    res_set = set()
    for i in dictionary:
        if dictionary[i] == count:
            res_set.add(i)
    return res_set


def get_randoms(divby: int) -> int:
    """
    Return a random number ranged between 1 and 1000 that is divisable by divby.
    Generate numbers using np.random.randint until you get such a number.
    """
    rnd = np.random.randint(1, 1001)
    while rnd % divby != 0:
        rnd = np.random.randint
    return rnd


def inner_product_r(v1: Iterable[float], v2: Iterable[float]) -> float:
    return sum(map(lambda t: t[0] * t[1], zip(v1, v2)))


def inner_product_c(c1: Iterable[complex], c2: Iterable[complex]) -> complex:
    return sum(map(lambda t: t[0] * t[1].conjugate(), zip(c1, c2)))


v = np.array([complex(8, 3), complex(-2, 91), complex(3, -2), complex(4, 0)])
u = np.array([complex(3.1, 1.4), complex(3, -9), complex(0, -21), complex(1, 12)])
res_vdot = np.vdot(u, v)
res_custom = inner_product_c(v, u)
assert np.vdot(u, v) == inner_product_c(v, u)
