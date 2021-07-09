def num_find(a):
    for_return=1

    if a==1:
        for_return=-1
    if a%2==0:
        for_return=-1
    for i in range(3,int(a/2),2):
        if a%i ==0:
            for_return=-1

    return for_return

while True:
    num=int(input(""))
    if num==0:
        break
    count=0
    for i in range(num+1,2*num+1):
        if num_find(i)==1:
            count+=1
    
    print(count)