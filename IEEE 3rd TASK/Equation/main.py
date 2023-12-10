def pow(x, y):
    result = 0
    for i in range(2, y + 1, 2):
        result += x ** i
    return result


num1, num2 = map(int, input().split())
print(pow(num1, num2))
