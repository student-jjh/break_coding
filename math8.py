def sugar(n):
    count=0
    while n>0:
        
        if (n)%5==0:
            count+=(n)/5
            return int(count)
        n=n-3
        count+=1
    if n==0:
        return count
    else:
        return -1

a=int(input(""))
print(sugar(a))