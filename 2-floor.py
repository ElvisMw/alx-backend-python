#!/usr/bin/env python3
"""
2-floor module
Contains a type-annotated function floor that
takes a float and returns its floor
"""
import math


def floor(n: float) -> int:
    """Returns the floor of a float"""
    return math.floor(n)


if __name__ == "__main__":
    ans = floor(3.14)
    print(ans)
