def num_find(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1,1):
        if a%i ==0:
            return False
    return True

while True:
    num=int(input(""))
    if num==0:
        break
    count=0
    for i in range(num+1,2*num+1):
        if num_find(i):
            count+=1
    
    print(count)