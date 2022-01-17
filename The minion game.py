def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    for index in range(len(string)):
        if string[index] in "AEIOU":
            kevin_score += length - index
        else:
            stuart_score += length - index

    if stuart_score < kevin_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")




if __name__ == '__main__':
    s = input()
    minion_game(s)