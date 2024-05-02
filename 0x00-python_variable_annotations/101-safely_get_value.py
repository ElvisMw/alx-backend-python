#!/usr/bin/env python3
"""TypeVar repesentation"""
from typing import Mapping, Any, TypeVar, Union, Optional

""" Define a TypeVar to represent the type of the
default parameter
"""
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """
    Returns the value associated with the given key in the
    dictionary if it exists, otherwise returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
