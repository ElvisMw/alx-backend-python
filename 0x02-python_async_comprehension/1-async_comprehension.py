#!/usr/bin/env python3
"""
Async Comprehensions
"""
import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using
    async comprehension.
    """
    return [number async for number in async_generator()]
