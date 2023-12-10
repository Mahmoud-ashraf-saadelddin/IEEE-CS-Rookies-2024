def swap_raw(arr, num1, num2, size):
    for i in range(size):
        temp = arr[num1][i]
        arr[num1][i] = arr[num2][i]
        arr[num2][i] = temp


def swap_column(arr, num1, num2, size):
    for i in range(size):
        temp = arr[i][num2]
        arr[i][num2] = arr[i][num1]
        arr[i][num1] = temp


def print_matrix(arr, size):
    for i in range(size):
        for z in range(size):
            print(arr[i][z], end=" ")
        print()


size, num1, num2 = map(int, input().split())

arr = []
for _ in range(size):
    row = list(map(int, input().split()))
    arr.append(row)

num1 -= 1
num2 -= 1

swap_raw(arr, num1, num2, size)
swap_column(arr, num1, num2, size)
print_matrix(arr, size)
