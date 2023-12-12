from math import factorial

a, b = map(int, input().split())

fac_A = factorial(a)
fac_B = factorial(b)
s = int(a - b)
fac = factorial(s)
permutation = int(fac_A / fac)
combination = int(permutation / fac_B)
print(combination, permutation)
