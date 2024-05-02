#!/usr/bin/env python3
"""
5-sum_list module
Contains a type-annotated function sum_list that
takes a list of floats and returns their sum
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats"""
    return sum(input_list)


if __name__ == "__main__":
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum)
