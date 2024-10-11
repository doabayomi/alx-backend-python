#!/usr/bin/env python3
"""Duck typing iterable object"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns an expanded view of an iterable object

    Args:
        lst: Iterable object

    Returns:
        a list containing a tuple of each element and their respective
        elements.
    """
    return [(i, len(i)) for i in lst]
