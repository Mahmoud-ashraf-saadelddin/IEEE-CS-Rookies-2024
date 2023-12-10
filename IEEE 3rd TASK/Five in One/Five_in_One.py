def count_divisor(num):
    m = num // 2
    counter = 0
    for z in range(1, m + 1):
        if num % z == 0:
            counter += 1
    return counter


def palindrome(num):
    temp = num
    sum_ = 0
    while num > 0:
        d = num % 10
        sum_ = (sum_ * 10) + d
        num //= 10
    return temp == sum_


size = int(input())
arr = list(map(int, input().split()))

arr.sort()
print("The maximum number :", arr[-1])
print("The minimum number :", arr[0])

count_prime = 0
count_palindrome = 0
for num in arr:
    if palindrome(num):
        count_palindrome += 1

    m = num // 2
    flag = 0
    for z in range(2, m + 1):
        if num % z == 0:
            flag = 1
            break
    if flag == 0 and num != 1:
        count_prime += 1

print("The number of prime numbers :", count_prime)
print("The number of palindrome numbers :", count_palindrome)

max_divisor_count = 0
max_divisor_num = arr[0]
for num in arr:
    c = count_divisor(num)
    if c >= max_divisor_count:
        max_divisor_count = c
        max_divisor_num = num

print("The number that has the maximum number of divisors :", max_divisor_num)
