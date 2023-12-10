size = int(input())  # Input size of array
arr = list(map(int, input().split()))  # Input array elements

minimum = arr[0]
maximum = arr[0]
min_index = 0
max_index = 0

for i in range(1, size):
    if minimum > arr[i]:
        minimum = arr[i]
        min_index = i
    if maximum < arr[i]:
        maximum = arr[i]
        max_index = i

arr[min_index] = maximum
arr[max_index] = minimum

for i in range(size):
    print(arr[i], end=" ")
