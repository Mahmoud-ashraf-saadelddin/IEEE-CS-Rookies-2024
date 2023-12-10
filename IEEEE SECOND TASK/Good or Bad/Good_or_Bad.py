words = int(input())
while words > 0:
    word = input()
    size = len(word)
    flag = 0
    for i in range(size - 2):
        if (word[i] == '0' and word[i + 1] == '1' and word[i + 2] == '0') or \
           (word[i] == '1' and word[i + 1] == '0' and word[i + 2] == '1'):
            flag = 1
            break
    if flag == 1:
        print("Good")
    else:
        print("Bad")
    words -= 1
