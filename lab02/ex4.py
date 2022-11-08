from typing import Iterable


def inner_product_c(c1: Iterable[complex], c2: Iterable[complex]) -> complex:
    return sum(map(lambda t: t[0] * t[1].conjugate(), zip(c1, c2)))
