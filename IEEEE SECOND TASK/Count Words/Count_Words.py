input1 = input()
n = [",", " ", "!", ".", "?"]
m = 1
counter = 0
for x in input1:
    if f"{x}" in f"{n}":
        counter += 1
for k in input1:
    if k in n:
        if f"{input1[m:m + 1]}" in n:
            counter -= 1
    m += 1
print(counter)
