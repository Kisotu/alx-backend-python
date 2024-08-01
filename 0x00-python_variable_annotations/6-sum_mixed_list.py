#!/usr/bin/env python3
"""Function sum_mixed_list that takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of list as a float"""
    return float(sum(mxd_lst))
