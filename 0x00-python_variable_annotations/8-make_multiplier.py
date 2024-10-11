#!/usr/bin/env python3
"""Function to make a custom multiply function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a  custom multiplication function

    Args:
        multiplier: Value to multiply by

    Returns:
        Returns a function that takes a float returns the number
        multiplied by the multiplier
    """
    def multiply(num: float):
        return float(multiplier * num)
    return multiply
