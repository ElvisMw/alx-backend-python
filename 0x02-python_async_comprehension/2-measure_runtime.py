#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
from time import perf_counter
from typing import List
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime for executing async_comprehension
    four times in parallel using asyncio.gather.
    """
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = perf_counter()
    return end_time - start_time
