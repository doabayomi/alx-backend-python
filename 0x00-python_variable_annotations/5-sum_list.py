#!/usr/bin/env python3
"""Sum of list of floats function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of elements in list of float

    Args:
        input_list: List of floats

    Returns:
        Sum of elements in list of floats
    """
    sum: float = 0
    for element in input_list:
        sum += element

    return sum
