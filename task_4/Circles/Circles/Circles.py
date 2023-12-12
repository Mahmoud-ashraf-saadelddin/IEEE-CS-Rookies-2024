x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
z1 = (x1 + x2) / 2
z2 = (y1 + y2) / 2
z3 = (x3 + x4) / 2
z4 = (y3 + y4) / 2
dia1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
rad1 = dia1 / 2  # calculate the radius of first circle
dia2 = ((x3 - x4) ** 2 + (y3 - y4) ** 2) ** 0.5
rad2 = dia2 / 2  # calculate the radius of second circle
summ = rad1 + rad2  # sum of two radius
# calculate the distance between two centers

distance = ((z1 - z3) ** 2 + (z2 - z4) ** 2) ** 0.5

if distance <= summ:
    print("YES", end="")
else:
    print("NO", end="")
