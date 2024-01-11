#!/usr/bin/env python3
""" TypeVar """
from typing import Mapping, TypeVar, Union, Any


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar, None] = None) -> Union[Any, TypeVar]:
    if key in dct:
        return dct[key]
    else:
        return default
