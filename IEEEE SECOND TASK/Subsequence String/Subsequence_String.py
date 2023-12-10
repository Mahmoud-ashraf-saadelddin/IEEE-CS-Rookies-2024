value = input()

my_value = "hello"
i = 0
z = 0

while True:
    if i == len(value) or z == len(my_value):
        break
    if value[i] == my_value[z]:
        z += 1
    i += 1

if z == 5:
    print("YES")
else:
    print("NO")
