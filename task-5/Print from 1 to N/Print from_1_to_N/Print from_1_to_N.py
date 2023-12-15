num = int(input())
def print_to_n(num):
    if num==1:
        return num
    else:
        return f"{print_to_n(num - 1)}\n{num}"

print(print_to_n(num),end="")
