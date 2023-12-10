testCases = int(input())
for _ in range(testCases):
    result = 0
    flag = 1
    size = int(input())
    arr = list(map(int, input().split()))
    min_val = float('inf')
    for z in range(1, size):
        for x in range(z + 1, size + 1):
            result = (arr[z - 1] + arr[x - 1]) + (x - z)
            if flag == 0 and min_val > result:
                min_val = result
            if flag:
                min_val = result
                flag = 0
            result = 0
    flag = 1
    print(min_val)
