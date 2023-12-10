Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
Original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

flag = int(input())
value = input()

size = len(value)
g = 0

if flag == 1:
    for i in range(size):
        for g in range(len(Original)):
            if value[i] == Original[g]:
                break
        print(Key[g], end='')
else:
    for i in range(size):
        for g in range(len(Key)):
            if value[i] == Key[g]:
                break
        print(Original[g], end='')
