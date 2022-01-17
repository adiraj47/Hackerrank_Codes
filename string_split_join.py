def split_and_join(line):
    # write your code here
    temp = line.split()

    join_str = "-".join(temp)
    return join_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)