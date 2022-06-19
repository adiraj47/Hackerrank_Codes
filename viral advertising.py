#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    initial_value = 5
    liked_value = 0
    for i in range(1, n+1):
        temp = initial_value // 2
        initial_value = temp * 3
        liked_value += temp
    return  liked_value

if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)
    print(result)

