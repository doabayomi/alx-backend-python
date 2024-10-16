#!/usr/bin/env python3
"""Measuring the coroutines runtime"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the run time of a wait_n instance

    Args:
        n: The number of wait_random instances in the wait_n instance
        max_delay: The max delay for the wait_random instances

    Returns:
        float: The runtime for the wait_n instance
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter() - start_time
    return end_time
