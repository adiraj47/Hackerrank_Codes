n = int(input())
if 1 <= n <= 100:
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        else:
            if 6 <= n <= 20:
                print("Weird")
            else:
                print("Not Weird")

