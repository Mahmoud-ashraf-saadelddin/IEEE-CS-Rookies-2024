def print1(arr, shift1, size):
    for i in range(shift1, size):
        print(arr[i], end=" ")


def print2(arr, shift2):
    for i in range(shift2):
        print(arr[i], end=" ")


size, times = map(int, input().split())
arr = list(map(int, input().split()))

sh = times % size

print1(arr, size - sh, size)
print2(arr, size - sh)
