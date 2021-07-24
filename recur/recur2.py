def pibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return pibo(n-1)+pibo(n-2)

a=int(input(''))
print(pibo(a))