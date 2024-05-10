#!/usr/bin/env python3
''' 1-async_comprehension '''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async comprehension that yields 10 random
    floating-point numbers between 0 and 10."""
    return [num async for num in async_generator()]
