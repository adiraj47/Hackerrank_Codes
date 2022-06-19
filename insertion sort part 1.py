#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    temp = arr[-1]
    count = n - 2
    deletevar = arr[count]

    while temp < arr[count]:
        arr[count + 1] = arr[count]
        count -= 1
        for element in arr:
            print(element, end=" ")
        print()
        if count == -1:
            break

    arr[count + 1] = temp
    for element in arr:
        print(element, end=" ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
