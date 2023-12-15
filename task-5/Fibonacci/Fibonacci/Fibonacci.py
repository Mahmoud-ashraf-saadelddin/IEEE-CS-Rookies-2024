n = int(input())


def Fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num >= 3:
        return Fibonacci(num - 1) + Fibonacci(num - 2)

print(Fibonacci(n))
