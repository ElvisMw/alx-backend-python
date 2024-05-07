#!/usr/bin/env python3
"""
This module contains two coroutines and one function for measuring execution time.

The wait_random() coroutine generates a random delay between 0 and max_delay
(inclusive), and then waits for that many seconds using asyncio.sleep().

The wait_n() coroutine creates a list of n coroutines, each of which calls
wait_random() with the same max_delay, and then waits for all of the coroutines
to complete using asyncio.gather().

The measure_time() function measures the total execution time of running
wait_n(n, max_delay) using asyncio.run(), and then returns total_time / n.
"""

import asyncio
import time
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random delay between 0 and max_delay, and waits for that many
    seconds using asyncio.sleep().

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
    Executes multiple coroutines at the same time using async.

    This function creates a list of n coroutines, each of which calls
    wait_random() with the same max_delay, and then waits for all of the
    coroutines to complete using asyncio.gather().

    Arguments:
        n: The number of tasks to create.
        max_delay: The maximum delay to pass to each task.

    Returns:
        The sorted list of wait times.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*coroutines)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns
    total_time / n.

    Arguments:
        n: The number of tasks to create.
        max_delay: The maximum delay to pass to each task.

    Returns:
        The average execution time per task.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
