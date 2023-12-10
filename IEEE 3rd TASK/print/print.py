num = int(input())


def pr(number):
    for i in range(1, number + 1):
        if i != 1:
            print(" ", end="")
        print(i, end="")


pr(num)
