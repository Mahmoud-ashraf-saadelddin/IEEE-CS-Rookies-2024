from math import gcd

a, b = map(int, input().split())
x = gcd(a, b)
lcm_value = (a * b) // x
print(x, lcm_value)

