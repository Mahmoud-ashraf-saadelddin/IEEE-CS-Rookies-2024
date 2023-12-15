test = int(input())
while test > 0:
    x = list(map(int, input()))
    l = len(x)


    def print_digit(x, l):
        if l == 1:
            return x[0]
        else:
            return f"{print_digit(x, l - 1)} {x[l - 1]}"



    for i in range(test):
        if test == 1:
            print(print_digit(x, l),end="")
            break
        else:
            print(print_digit(x, l))
            break

    test -= 1
