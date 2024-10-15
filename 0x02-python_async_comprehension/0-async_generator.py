#!/usr/bin/env python3
"""Creating asynchronous generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times and yields a random number

    Returns:
        None

    Yields:
        A random number between 0 and 10
    """
    for _ in range(10):
        asyncio.sleep(1)
        yield random.uniform(0, 10)
