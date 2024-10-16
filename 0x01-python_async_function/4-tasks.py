#!/usr/bin/env python3
"""Task based implementation of wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Tasked version of wait_n implementation

    Args:
        n: Number of wait_random instances
        max_delay: Max delay for each wait_random instance

    Returns:
        A lists of all delay instances in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = list()

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
