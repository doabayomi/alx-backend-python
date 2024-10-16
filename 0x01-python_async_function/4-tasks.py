#!/usr/bin/env python3
"""Task based implementation of wait_n"""
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n: _description_
        max_delay: _description_

    Returns:
        _description_
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = list()

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
