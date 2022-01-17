#!/bin/python3

import math
import os
import random
import re
import sys
# def athelete_sort(score, sort_column):
#     """
#     The sorting fo the score data according to the column
#     :param score: The raw unsorted list
#     :param sort_column: column according to which sorting needs to be done
#     :return: sorted list
#     """
#     for index in range(len(score)):
#         min_idx = index
#
#         for j in range(index + 1, len(score)):
#             if score[min_idx][sort_column] > score[j][sort_column]:
#                 min_idx = j
#
#         score[index], score[min_idx] = score[min_idx], score[index]
#     return score
def value_column(val):
    return val[k]


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=value_column)
    print(arr)
    # result = athelete_sort(arr, k)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()
