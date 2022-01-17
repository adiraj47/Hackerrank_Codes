if __name__ == '__main__':
    s1 = input()
    s = list(s1)
    # for i in s:
    #     if str(i).isalnum():
    #         print(True)
    #         break
    # else:
    #     print(False)
    # for i in s:
    #     if str(i).isalpha():
    #         print(True)
    #         break
    # else:
    #     print(False)
    # for i in s:
    #     if str(i).isdigit():
    #         print(True)
    #         break
    # else:
    #     print(False)
    #
    # for i in s:
    #     if str(i).islower():
    #         print(True)
    #         break
    # else:
    #     print(False)
    # for i in s:
    #     if str(i).isupper():
    #         print(True)
    #         break
    # else:
    #     print(False)
    print(any([char.isalnum() for char in s]))
    print(any([char.isalpha() for char in s]))
    print(any([char.isdigit() for char in s]))
    print(any([char.islower() for char in s]))
    print(any([char.isupper() for char in s]))


    # print(s.isalnum())
    # print(s.isalpha())
    # print(s.isdigit())
    # print(s.islower())
    # print(s.isupper())

