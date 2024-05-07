#!/usr/bin/env python3
"""Asynchronous coroutine that generates a random delay
between 0 and max_delay.
"""
import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Arguments:
        max_delay: The maximum delay to generate (defaults to 10).

    Returns:
        The delay that was generated.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines at the same time with async.

    This function generates a list of n random delays between 0 and max_delay,
    creates a list of asyncio Tasks, each of which runs the wait_random
    coroutine with the generated delay, waits for all of the tasks to complete,
    and returns the sorted list of wait times.

    Arguments:
        n: The number of tasks to create.
        max_delay: The maximum delay to pass to each task.

    Returns:
        The sorted list of wait times.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
