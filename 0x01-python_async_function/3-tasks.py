#!/usr/bin/env python3

"""
Import the wait_random function from the 0-basic_async_syntax module
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a new asyncio Task that runs the wait_random coroutine.

    The created Task will run the wait_random function with the given
    max_delay argument.

    Arguments:
        max_delay: The maximum delay to pass to the wait_random function.

    Returns:
        The created asyncio Task.
    """

    return asyncio.create_task(wait_random(max_delay))
