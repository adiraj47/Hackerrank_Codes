from mutations_hackerrank import mutate_string
# def minion_game(string):
#     counter_stuart = 0
#     counter_kevin = 0
#     vowels = "AEIOU"
#     l = len(string)
#     for index, val in enumerate(string):
#         if val in vowels:
#             for k in range(index, l):
#                 print(string[index])
#                 counter_kevin += 1
#         else:
#             for k in range(index, l):
#                 counter_stuart += 1
#     if counter_stuart > counter_kevin:
#         print("Stuart {0}".format(counter_stuart))
#     elif counter_stuart < counter_kevin:
#         print("Kevin {0}".format(counter_kevin))
#     else:
#         print("Draw")
#
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)