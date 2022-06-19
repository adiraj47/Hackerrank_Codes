#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s:str, n:int):
    # Write your code here
    count_of_a = s.count('a')
    size_str = len(s)
    istr_size = n / size_str
    ans = int(istr_size) * count_of_a
    temp = n - (int(istr_size) * size_str)
    remain_str = s[:temp]
    ans += remain_str.count('a')
    return ans


if __name__ == '__main__':

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)
    print(result)


