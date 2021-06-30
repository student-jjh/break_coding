#분수찾기 
k=int(input(""))

n=1
if k==1:
    print('1/1')
else:
    while (n+1)*(n+2)/2 < k:
        n+=1

    need=k-((n)*(n+1)/2)-1
    if (n+1)%2==0: 
        x=int(1+need)
        y=int(n+1-need)

    else:
        x=int(n+1-need)
        y=int(1+need)


    print(str(x)+'/'+str(y))
