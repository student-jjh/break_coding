while True:
    word = input("")
    if word == '0':
        break
    for i in range(len(word)):
        if word[i] != word[-1-i]:
            print("no")
            break
    if i == len(word)-1:
        print("yes")    