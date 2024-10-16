#!/usr/bin/env python3
"""Task based implementation of wait_random"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """Executes wait_random as an asyncio task

    Args:
        max_delay: Max delay for wait_random

    Returns:
        The task object created
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
