def reach(num):
    global value
    if value < num:
        return False
    elif value == num:
        return True
    else:
        return reach(num * 10) or reach(num * 20)
test = int(input())
while test > 0:
    value = int(input())
    flag = reach(1)

    if flag:
        print("YES")
    else:
        print("NO")
    test -= 1

