#!/usr/bin/env python3
"""
Module that measures the runtime of four calls to async_comprehension
"""
import asyncio
import time
from importlib import import_module as using


"""Async function that collects 10 random numbers"""
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of four calls to
    async_comprehension
    """

    start_time = time.time()

    """ Executes 4 calls to async_comprehension concurrently
    gather() returns a list of futures"""
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    """ Subtract start time from current time to get total runtime"""
    return time.time() - start_time
