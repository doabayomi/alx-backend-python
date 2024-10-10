#!/usr/bin/env python3
from typing import List
"""Sum of elements in mixed list"""

def sum_mixed_list(mxd_lst: List[int, float]) -> float:
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
