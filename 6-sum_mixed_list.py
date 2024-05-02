#!/usr/bin/env python3
"""
6-sum_mixed_list module
Contains a type-annotated function sum_mixed_list
that takes a list of integers and floats and returns their sum
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floats"""
    return sum(mxd_lst)


if __name__ == "__main__":
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans)
