def ara(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return a

def pal(n):
    for i in range(0,len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True
array_for_answer=ara(10000000)

N=int(input(""))

for i in range(N,1000001,1):
    if array_for_answer[i] and pal(str(i)):
        print(i)
        break

