#!/usr/bin/env python3
"""
Asynchronous coroutine that generates a random delay
between 0 and max_delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function generates a random delay using the
    built-in random.uniform function and then waits for
    that many seconds using the asyncio.sleep function.

    The function returns the delay that was generated.

    Arguments:
        max_delay: The maximum delay to generate (defaults to 10).

    Returns:
        The delay that was generated.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
