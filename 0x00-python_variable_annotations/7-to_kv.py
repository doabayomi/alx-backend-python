#!/usr/bin/env python3
"""Function for string and float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple of k and v

    Args:
        k: A string
        v: A float or int

    Returns:
        Tuple containing k and v
    """
    return (k, float(v * v))
