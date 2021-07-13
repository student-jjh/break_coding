def ara(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return a

array_for_answer=ara(246912)

while True:
    k=int(input(""))
    if k==0:
        break
    count=0
    for i in range(k,k*2+1,1):
        if array_for_answer[i]:
            count+=1
    print(count)