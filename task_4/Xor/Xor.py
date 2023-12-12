a, b, q = map(int, input().split())
x = q % 3
if x == 1:
    print(a)
elif x == 2:
    print(b)
else:
    print(a ^ b)
