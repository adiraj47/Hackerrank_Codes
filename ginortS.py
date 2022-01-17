def ginsort(arr):

    sorted_str = ""
    lower_str = ""
    upper_str = ""
    numerical_str = ""
    even_numerical_str = ""
    odd_numerical_str = ""
    # lower string
    for char in arr:
        if 97 <= ord(char) <= 122:
            lower_str += char
        elif 65 <= ord(char) <= 90:
            upper_str += char
        else:
            numerical_str += char
    numerical_str = "".join(sorted(numerical_str))
    for value in numerical_str:
        if int(value) % 2 == 0:
            even_numerical_str += value
        else:
            odd_numerical_str += value

    sorted_str = "".join(sorted(lower_str) + sorted(upper_str)) + odd_numerical_str + even_numerical_str

    return sorted_str


if __name__ == "__main__":
    unsorted_str = input()
    return_str = ginsort(unsorted_str)
    print(return_str)