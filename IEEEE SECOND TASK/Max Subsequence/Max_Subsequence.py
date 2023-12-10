size = int(input())
n = input()
if size == len(n):
    m = 1
    counter = 0
    for x in n:
        if f"{x}" == f"{n[m:m + 1]}":
            pass
        else:
            counter += 1
        m += 1

    print(counter)

