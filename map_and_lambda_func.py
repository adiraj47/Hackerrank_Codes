cube = lambda x: x ** 3# complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    if n <= 1:
        if n == 0:
            return []
        else:
            return [0]
    new_list = [0, 1]

    for index in range (2, n ):
        temp = new_list[-1] + new_list[-2]
        new_list.append(temp)

    return new_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))