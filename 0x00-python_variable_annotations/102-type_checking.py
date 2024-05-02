#!/usr/bin/env python3
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in on an array by a given factor.

    Args:
        lst (tuple): The array to be zoomed in on.
        factor (int, optional): The factor of zoom. Defaults to 2

    Returns:
        tuple: The zoomed in array.
    """
    zoomed_in: Tuple[int, ...] = tuple(item for item in lst for _ in range(factor))
    return zoomed_in
