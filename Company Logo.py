#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    arr = list(s)
    arr.sort()
    count_dict = {}
    for ele in arr:
        if ele in count_dict:
            count_dict[ele] += 1
        else:
            count_dict[ele] = 1
    k = Counter(count_dict)
    high_score = k.most_common(3)


    # unique_chars = set(s)
    # count_dict = {}
    #
    # for value in unique_chars:
    #     count_dict[value] = s.count(value)
    #
    # k = Counter(count_dict)
    # high_score = k.most_common(3)
    for items in high_score:
        print(f"{items[0]} {items[1]}")


