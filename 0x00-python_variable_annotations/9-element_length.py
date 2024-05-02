#!/usr/bin/env python3
"""
9-element_length module
Contains a type-annotated function element_length
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element of the
    input sequence `lst` and its length.

    Parameters:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains a sequence from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
