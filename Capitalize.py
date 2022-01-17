def solve(s: str) -> str:
    """
    The string which will contain the first n last name will be be passed and its first letters will be capitalized
    :param s: conatains the string with first and second name
    :return: first and last name capitalized
    """

    temp = ""
    string_list = []
    new_string = ""
    for char in s:
        if char == " ":
            if len(temp) != 0:
                string_list.append(temp)
            string_list.append(" ")
            temp = ""
            continue
        temp += char
    string_list.append(temp)
    print(string_list)
    for element in string_list:
        if element == " ":
            new_string += " "
        else:
            new_string += element[0].upper() + element[1:]
    return new_string


full_name = "hello  world lol"
print(solve(full_name))