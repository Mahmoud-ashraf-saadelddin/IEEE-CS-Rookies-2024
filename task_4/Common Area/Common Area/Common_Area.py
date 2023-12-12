testCase = int(input())
counter = 1

while counter <= testCase:
    numR = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    maxx1, maxy1, minx2, miny2 = x1, y1, x2, y2

    for i in range(1, numR):
        x1, y1, x2, y2 = map(int, input().split())
        maxx1 = max(maxx1, x1)
        maxy1 = max(maxy1, y1)
        minx2 = min(minx2, x2)
        miny2 = min(miny2, y2)

    if minx2 > maxx1 and miny2 > maxy1:
        print(f"Case #{counter}: {(minx2 - maxx1) * (miny2 - maxy1)}")
    else:
        print(f"Case #{counter}: {0}")

    counter += 1
