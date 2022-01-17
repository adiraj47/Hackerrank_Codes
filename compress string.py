import itertools

data = input()
output = []
x = itertools.groupby(data)

for key, value in x:
    output.append((len(list(value)), int(key)))

for element in output:
    print(element, end=" ")
