#!/usr/bin/env python3
"""
9-element_length module
Contains a type-annotated function element_length
"""
from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence, int]]:
    """Annotates the function element_length"""
    return [(i, len(i)) for i in lst]
