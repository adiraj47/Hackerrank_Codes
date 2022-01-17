if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    # print(students)
    students.sort(key=lambda x: x[1])
    second_lowest = students[0][1]
    for i in students:
        name, score = i
        if second_lowest < score:
            second_lowest = score
            break
    lowest_name = []
    # print(second_lowest)
    for i in range (len(students)):
        if second_lowest == students[i][1]:
            lowest_name.append(students[i][0])
    lowest_name.sort()
    for name in lowest_name:
        print(name)









