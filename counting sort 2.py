#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    result = [0] * 100
    unique_ele = set(arr)
    for element in unique_ele:
        temp = arr.count(element)
        result[element] = temp
    for index in range(len(result)):
        element = result[index]
        if element != 0:
            for j in range(element):
                print(index, end=' ')




if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)


