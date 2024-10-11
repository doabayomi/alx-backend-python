#!/usr/bin/env python3
"""Sum of elements in mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of elements in mixed list

    Args:
        mxd_lst: Mixed list of integers and floats

    Returns:
        Sum of elements in mixed list
    """
    sum: float = 0
    for element in mxd_lst:
        sum += float(element)

    return sum
