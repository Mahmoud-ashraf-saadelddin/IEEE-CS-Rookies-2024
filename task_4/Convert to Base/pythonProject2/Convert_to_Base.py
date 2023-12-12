def num(c):
    if c.isdigit():
        return int(c)
    else:
        return ord(c.upper()) - ord('A') + 10

def num2(num):
    if num < 10:
        return str(num)
    else:
        return chr(num - 10 + ord('A'))

def to_dec(value, base):
    size = len(value)
    power = 1
    result = 0
    for i in range(size - 1, -1, -1):
        result += num(value[i]) * power
        power *= base
    return result

def from_dec(number, base):
    res = []
    while number > 0:
        res.append(num2(number % base))
        number //= base
    res.reverse()
    return ''.join(res)

ca = int(input())
if ca == 1:
    arr, base = input().split()
    base = int(base)
    print(to_dec(arr, base),end="")
else:
    number, base = map(int, input().split())
    print(from_dec(number, base),end="")

