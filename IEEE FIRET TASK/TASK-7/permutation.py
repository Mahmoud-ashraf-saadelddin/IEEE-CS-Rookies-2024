size = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

flag = 0
for i in range(size):
    if arr1[i] != arr2[i]:
        flag = 1
        break

if flag == 0:
    print("yes")
else:
    print("no")
