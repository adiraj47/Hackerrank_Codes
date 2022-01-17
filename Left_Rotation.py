def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        temp = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[-1] = temp
    print(arr)



arr1= [1, 2, 3, 4, 5]
d = 2
rotateLeft(d, arr1)