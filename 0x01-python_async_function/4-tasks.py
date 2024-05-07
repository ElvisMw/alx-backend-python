#!/usr/bin/env python3
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def task_wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that generates a random delay
    between 0 and max_delay.
    """
    return await wait_random(max_delay)

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines at the same time with async
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
