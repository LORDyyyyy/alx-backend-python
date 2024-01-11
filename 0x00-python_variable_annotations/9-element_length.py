#!/usr/bin/env python3
""" idk """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ idk """
    return [(i, len(i)) for i in lst]
