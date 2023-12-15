number = int(input())
k = list(map(int, input().split()))


def avg(arr):
    c = 0
    sum = 0
    for i in range(len(arr)):
        c += 1
        sum += arr[i]
    return sum / c


def sequence(num, l):
    if num == 1:

        return f"{avg(l):0.6f}"
    else:

        return f"{sequence(num - 1, l)}"


print(sequence(number, k), end="")
