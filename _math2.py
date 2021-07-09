def num_find(a):
    for_return=1

    if a==1:
        for_return=-1
    for i in range(2,a,1):
        if a%i ==0:
            for_return=-1

    return for_return

M=int(input(""))
N=int(input(""))
min=-1
sum=0
for i in range(N,M-1,-1):
    if num_find(i)==1:
        sum+=i
        min=i
    
if min==-1:
    print(-1)
else:
    print(sum)
    print(min)
