def result(weigth, arr1, arr2, size):
    if weigth == 0 or size == 0:
        return 0
    if arr1[size - 1] > weigth:
        return result(weigth, arr1, arr2, size - 1)
    else:
        return max(
            arr2[size - 1] + result(weigth - arr1[size - 1], arr1, arr2, size - 1),
            result(weigth, arr1, arr2, size - 1)
        )


size, weigth = map(int, input().split())
arr1 = []
arr2 = []
for i in range(size):
    x, y = map(int, input().split())
    arr1.append(x)
    arr2.append(y)
print(result(weigth, arr1, arr2, size))
