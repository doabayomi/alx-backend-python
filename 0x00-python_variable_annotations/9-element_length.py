#!/usr/bin/env python3
from typing import Iterable, Sequence, Tuple
"""Duck typing iterable object"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns an expanded view of an iterable object

    Args:
        lst: Iterable object

    Returns:
        a list containing a tuple of each element and their respective
        elements.
    """
    return [(i, len(i)) for i in lst]
