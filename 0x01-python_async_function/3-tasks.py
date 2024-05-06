#!/usr/bin/env python3

import asyncio
from typing import Task
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that generates a random
    delay between 0 and max_delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Task:
    """
    Function that creates and returns an asyncio.
    Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
