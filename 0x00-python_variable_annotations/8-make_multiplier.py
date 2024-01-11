#!/usr/bin/env python3
""" idk """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a type-annotated function sum_list which takes a list of floats as argument
    and returns their sum as a float.
    """
    def func(multiplier: float) -> float:
        return (multiplier * multiplier)

    return (func)
