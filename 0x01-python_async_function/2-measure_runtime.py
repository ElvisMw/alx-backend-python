#!/usr/bin/env python3
"""
This module contains two coroutines and one function
for measuring execution time.
"""

import asyncio
import time
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random delay between 0 and max_delay,
    and waits for that many
    seconds using asyncio.sleep().
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines at the same time using async.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*coroutines)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns
    total_time / n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
