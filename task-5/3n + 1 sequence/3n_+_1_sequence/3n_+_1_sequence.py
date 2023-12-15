number = int(input())


def sequence(num,counter):

    if num == 1:
        counter += 1
        return f"{(counter)}"
    else:
        if (num % 2 == 0):
            counter += 1
            return f"{sequence(num / 2 , counter)} "
        else:
            counter += 1
            return f"{sequence(3 * num + 1 ,counter)} "


print(sequence(number,0),end="")
