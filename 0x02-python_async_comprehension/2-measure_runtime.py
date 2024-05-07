#!/usr/bin/env python3
""" 2-measure_runtime """
import asyncio
from time import perf_counter
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel.

    Returns:
        float: The total runtime of executing async_comprehension
        four times in parallel.
    """
    start_time = perf_counter()
    """ Executes async_comprehension four times in parallel """
    await asyncio.gather(
        *[async_comprehension() for _ in range(4)]
    )
    end_time = perf_counter()
    return end_time - start_time
