num1=int(input(""))
for j in range(num1):
    str1=input("")
    for_answer=0
    count=0
    for i in str1:
        if i =='O':
            count+=1
            for_answer+=count
        else:
            count=0

    print(for_answer)