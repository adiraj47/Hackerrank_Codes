def print_rangoli(size):
    # your code goes here
    string = ""
    width = size * 4 - 3
    for index in range(1, size + 1):
        for j in range(index):
            string += chr(96 + size - j)
            if len(string) < width:
                string += "-"
        # for k in range(index-1, 0, -1):
        #     string += chr(97 + size - k)
        #     if len(string) < width:
        #         string += "-"
        # print(string.center(width, "-"))
        print(string)
        string = ""

    for i



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)