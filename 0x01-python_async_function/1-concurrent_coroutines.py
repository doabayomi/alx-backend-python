#!/usr/bin/env python3
"""Executing multiple coroutines concurrently"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Executes multiple wait_random() instances

    Args:
        n: The number of instances
        max_delay: The max delay for the wait_random instances

    Returns:
        A list of delay times in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = list()

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
