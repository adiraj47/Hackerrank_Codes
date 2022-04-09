#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat1 = abs(x - z)
    cat2 = abs(y - z)
    if cat1 == cat2:
        return "Mouse C"
    else:
        if cat1 < cat2:
            return "Cat A"
        else:
            return "Cat B"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)

