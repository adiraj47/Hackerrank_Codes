#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here

    temp = set(ar)
    pairs = 0

    for value in temp:
        val = ar.count(value)
        if val != 1:
            pairs += int(val / 2)
    return pairs
if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)