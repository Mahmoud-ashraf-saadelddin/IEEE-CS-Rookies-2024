r1, c1 = map(int, input().split())
arr1 = []
for i in range(r1):
    row = list(map(int, input().split()))
    arr1.append(row)

r2, c2 = map(int, input().split())
arr2 = []
for i in range(r2):
    row = list(map(int, input().split()))
    arr2.append(row)

result = [[0 for _ in range(c2)] for _ in range(r1)]

for i in range(r1):
    for z in range(c2):
        for x in range(c1):
            result[i][z] += arr1[i][x] * arr2[x][z]

for i in range(r1):
    for z in range(c2):
        print(result[i][z], end=" ")
    print()
