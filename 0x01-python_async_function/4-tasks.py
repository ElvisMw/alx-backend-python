#!/usr/bin/env python3
"""
The task_wait_n function creates a list of asyncio Tasks, each of which runs
the task_wait_random function with the given max_delay argument.

The function then waits for all of the tasks to complete using asyncio.gather
and returns the sorted list of wait times.
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates a list of asyncio Tasks, waits for all of them to complete, and
    returns the sorted list of wait times.

    Arguments:
        n: The number of tasks to create.
        max_delay: The maximum delay to pass to each task.

    Returns:
        The sorted list of wait times.
    """

    wait_tasks = [task_wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*wait_tasks)
    return sorted(wait_times)
