#!/bin/python3



#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    for element in range(i, j + 1):
        temp = str(element)
        temp = temp[::-1]
        temp = int(temp)
        if abs(element - temp) % k == 0:
            count += 1

    return count


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)
    print(result)
