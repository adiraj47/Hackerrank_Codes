import textwrap


def wrap(string, max_width):
    count = 0
    new_string = ""
    temp = ""

    for value in string:
        temp += value
        count += 1
        if count == max_width:
            new_string += f"{temp}\n"
            count = 0
            temp = ""
    remaining_value = len(string) % max_width
    if remaining_value != 0:
        new_string += string[-remaining_value:]

    return new_string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)