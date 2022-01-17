if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        list_operation = input().casefold()
        list_split = list_operation.split()
        # print(list_split)
        if list_split[0] == "insert":
            arr.insert(int(list_split[1]), int(list_split[2]))
        elif list_split[0] == "print":
            print(arr)
        elif list_split[0] == 'remove':
            arr.remove(int(list_split[1]))

        elif list_split[0] == "append":
            arr.append(int(list_split[1]))

        elif list_split[0] == "sort":
            arr.sort()

        elif list_split[0] == "pop":
            arr.pop()

        elif list_split[0] == "reverse":
            temp = arr[::-1]
            arr = temp

        else:
            print("Invalid input")
            break



