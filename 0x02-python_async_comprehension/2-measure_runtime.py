#!/usr/bin/env python3
"""Measuring runtime of async_comprehension function"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime for async_comprehension()

    Returns:
        The total runtime of async_comprehension()
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter() - start_time
    return end_time
