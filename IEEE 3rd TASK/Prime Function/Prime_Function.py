import math


def prime(num):
    if num < 2:
        return "YES"
    new_number = int(math.sqrt(num))
    for i in range(2, new_number + 1):
        if num % i == 0:
            return "NO"
    return "YES"


test = int(input())
while test > 0:
    num = int(input())
    if num == 1:
        print("NO")
        test -= 1
        continue
    if num > 1:
        print(prime(num))
    test -= 1
