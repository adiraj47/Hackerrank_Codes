n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
sum_average = 0
if query_name in student_marks:
    for mark in student_marks[query_name]:
        sum_average += mark

    sum_average /= 3
    print("{:.2f}".format(sum_average))
