#!/usr/bin/env python3
""" 1-async_comprehension """
from typing import List
from random import uniform
from asyncio import gather
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension
    over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [number async for number in async_generator()]
