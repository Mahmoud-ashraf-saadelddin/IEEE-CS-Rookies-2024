size, sizeSqu = map(int, input().split())

arr = list(map(int, input().split()))
arrSqu = list(map(int, input().split()))

z = 0
counter = 0
for i in range(size):
    if z < sizeSqu and arr[i] == arrSqu[z]:
        counter += 1
        z += 1

if counter == sizeSqu:
    print("YES")
else:
    print("NO")
