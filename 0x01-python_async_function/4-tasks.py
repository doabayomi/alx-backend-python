#!/usr/bin/env python3
"""Task based implementation of wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


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
