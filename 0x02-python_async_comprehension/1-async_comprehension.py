#!/usr/bin/env python3
"""Collecting values from async_generator()"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects the 10 numbers sent from async_generator()

    Returns:
        List containing the 10 numbers from async_generator()
    """
    result = [i async for i in async_generator()]
    return result
