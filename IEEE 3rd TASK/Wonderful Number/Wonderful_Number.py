def binary(num):
    bin = []

    while num != 0:
        bin.append(num % 2)
        num //= 2

    return bin


def palindrome(arr):
    length = len(arr)
    for i in range(length // 2):
        if arr[i] != arr[length - i - 1]:
            return False
    return True


num = int(input())
if num % 2 == 0:
    print("NO")
else:
    binary = binary(num)
    if palindrome(binary):
        print("YES")
    else:
        print("NO")
