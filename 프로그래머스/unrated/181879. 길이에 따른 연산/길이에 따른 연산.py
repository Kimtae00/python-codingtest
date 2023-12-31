from functools import reduce
from operator import mul

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return reduce(mul, num_list, 1)
