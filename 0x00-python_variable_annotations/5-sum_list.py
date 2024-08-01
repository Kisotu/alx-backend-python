#!/usr/bin/env python3
"""Function sum_list thattakes a list
input_list of floats as argument and returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns their sum as a float
    '''
    return float(sum(input_list))
