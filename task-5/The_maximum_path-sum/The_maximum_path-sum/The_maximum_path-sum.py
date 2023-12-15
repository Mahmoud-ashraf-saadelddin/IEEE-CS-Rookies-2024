def maxPath(i, j):
    if i == row - 1 and j == column - 1:
        return arr[i][j]

    if i >= row or j >= column:
        return float('-inf')

    x = maxPath(i, j + 1)
    y = maxPath(i + 1, j)

    return arr[i][j] + max(x, y)


row, column = map(int, input().split())
arr = []
for i in range(row):
    values = list(map(int, input().split()))
    arr.append(values)

print(maxPath(0, 0), end="")
