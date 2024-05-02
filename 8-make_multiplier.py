#!/usr/bin/env python3
"""
8-make_multiplier module
Contains a type-annotated function make_multiplier that
takes a float and returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the multiplier"""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
