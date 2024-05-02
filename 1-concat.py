#!/usr/bin/env python3
"""
1-concat module
Contains a type-annotated function concat that
takes two strings and returns their concatenation
"""


def concat(str1: str, str2: str) -> str:
    """Concatenates two strings and returns the result"""
    return str1 + str2


if __name__ == "__main__":
    str1 = "egg"
    str2 = "shell"
    print(concat(str1, str2))
