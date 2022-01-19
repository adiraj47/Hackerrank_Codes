def design(row, column):
    oddcount = 1
    for i in range(int(row / 2)):
        pdash = "-" * int((column - (oddcount * 3)) / 2)
        print(f"{pdash}{'.|.' * oddcount}{pdash}", end="")
        print()
        oddcount += 2
    dashprint = int(((column - 7) / 2))
    dash = "-" * dashprint
    print(dash, end="")
    print("WELCOME", end="")
    print(dash)
    oddcount -= 2
    for i in range(int(row / 2)):
        pdash = "-" * int((column - (oddcount * 3)) / 2)
        print(f"{pdash}{'.|.' * oddcount}{pdash}", end="")
        print()
        oddcount -= 2


if __name__ == "__main__":
    dimensions = input()
    dimensions_list = dimensions.split()
    dimensions_list[0], dimensions_list[1] = int(dimensions_list[0]), int(dimensions_list[1])
    design(*dimensions_list)

