#!/usr/bin/env python3
""" sum of nums """
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
    a type-annotated function sum_list which takes a list of floats as argument
    and returns their sum as a float.
    """
    return (sum(input_list))
