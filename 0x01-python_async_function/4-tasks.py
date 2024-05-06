#!/usr/bin/env python3

import asyncio
from typing import List, Task
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that generates a random
    delay between 0 and max_delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that creates asyncio Tasks for wait_random and
    returns the list of delays.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in tasks]
