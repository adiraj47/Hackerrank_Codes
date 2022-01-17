if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr)
    sum1 = 0
    second_lowest = arr[0]
    for i in range(n):
        if second_lowest > arr[i]:
            second_lowest = arr[i]
            break

    print(second_lowest)




