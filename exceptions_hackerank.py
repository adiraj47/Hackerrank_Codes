if __name__ == "__main__":
    n = int(input())
    for i in range(n):

        digits = input("")

        split_digits = digits.split()
        try:
            first_digit = int(split_digits[0])
        except ValueError:
            print("Error Code: invalid literal for int() with base 10: '{}'".format(split_digits[0]))
            continue
        try:
            second_digit = int(split_digits[1])
        except ValueError:
            print("Error Code: invalid literal for int() with base 10: '{}'".format(split_digits[1]))
            continue
        try:
            division = first_digit / second_digit
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        else:
            print(int(division))




