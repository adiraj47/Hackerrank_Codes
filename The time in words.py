#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
def num_to_words(n):
    num2words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                 10: "ten",
                 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen",
                 17: "seventeen",
                 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "half", 45: "quarter"}
    try:
        return num2words[n]
    except KeyError:
        return f"{num2words[n-n % 10]} {num2words[n % 10]}"


def min_left(minutes):
    return 60 - minutes

def timeInWords(h, m):
    # Write your code here
    result = ""
    hour = num_to_words(h)
    if m > 30:
        hour = num_to_words(h + 1)
        if m == 45:
            minutes = num_to_words(m)

            result = f"{minutes} to {hour}"
        else:
            difference = min_left(m)
            minutes = num_to_words(difference)
            result = f"{minutes} minutes to {hour}"
    elif m == 00:
        result = f"{hour} o' clock"
    else:
        if m == 15 or m == 30:
            minutes = num_to_words(m)
            result = f"{minutes} past {hour}"
        elif m == 1:
            minutes = num_to_words(m)
            result = f"{minutes} minute past {hour}"
        else:
            minutes = num_to_words(m)
            result = f"{minutes} minutes past {hour}"
    return result





if __name__ == '__main__':

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)
    print(result)


