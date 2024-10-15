#!/usr/bin/env python3
"""Creating an synchronous generator yielding numbers"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times and yields a random number

    Yields:
        float: A random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
