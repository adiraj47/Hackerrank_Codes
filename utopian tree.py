#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    count = 1
    addition = 1
    while (count <= n):
        if count % 2 == 0:
            addition += 1
        else:
            addition *= 2

        count += 1
    return addition


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        print(result)
