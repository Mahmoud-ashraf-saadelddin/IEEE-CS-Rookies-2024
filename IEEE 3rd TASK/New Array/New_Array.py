def print_array(arr):
    print(' '.join(map(str, arr)), end=" ")


size = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print_array(arr2)
print_array(arr1)
