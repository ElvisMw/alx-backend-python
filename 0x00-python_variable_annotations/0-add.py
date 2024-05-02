#!/usr/bin/env python3
"""
0-add module
Contains a type-annotated function add that takes
two floats and returns their sum
"""


def add(a: float, b: float) -> float:
    """Adds two floats and returns their sum"""
    return a + b


if __name__ == "__main__":
    print(add(1.11, 2.22))
