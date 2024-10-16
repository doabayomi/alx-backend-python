#!/usr/bin/env python3
"""Randomly delayed corooutine"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay time

    Args:
        max_delay: Delay time between 0 and 10. Defaults to 10.

    Returns:
        The delay time waited
    """
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
