num1, num2 = map(int, input().split())
code = input()

if num1 + num2 + 1 != len(code):
    print("No")
    exit()

if code[num1] != '-':
    print("No")
    exit()

counter = 0
for i in range(len(code)):
    if code[i] >= '0' and code[i] <= '9' and i != num1:
        counter += 1

if counter == num1 + num2:
    print("Yes")
else:
    print("No")
