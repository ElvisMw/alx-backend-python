#!/usr/bin/env python3
""" 0-async_generator """
import asyncio
import random


async def async_generator() -> "asyncio.Future[float]":
    """
    Async generator that yields 10 random numbers
    between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
