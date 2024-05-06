#!/usr/bin/env python3

import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that generates a random
    delay between 0 and max_delay.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines at the same time.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*coroutines)
