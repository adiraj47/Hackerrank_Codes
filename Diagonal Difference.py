def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0
    # for left diagonal sum
    for i in range(len(arr)):
        left_diagonal += arr[i][i]

    # for right diagonal sum
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (i + j) == (n - 1):
                right_diagonal += arr[i][j]
    # to do the sum of the diagonals

    return abs((left_diagonal - right_diagonal))


n = int(input().strip())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
print(arr)  # TODO Delete this line

result = diagonalDifference(arr)
print(result) # TODO Delete this line
