#!/usr/bin/env python3
"""
10-safe_first_element module
Contains a type-annotated function safe_first_element
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Annotates the function safe_first_element"""
    if lst:
        return lst[0]
    else:
        return None
