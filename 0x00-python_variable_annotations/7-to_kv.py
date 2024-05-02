#!/usr/bin/env python3
"""
7-to_kv module
Contains a type-annotated function to_kv that takes a
string and an int or float and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string k and the
    square of the int or float v"""
    return (k, v ** 2)
