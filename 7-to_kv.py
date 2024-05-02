#!/usr/bin/env python3
"""
7-to_kv module
Contains a type-annotated function to_kv that takes a
string and an int or float and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string k and the square of the int or float v"""
    return (k, v ** 2)


if __name__ == "__main__":
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
