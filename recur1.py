def recur(n):
    if n==0:
        return 1
    else:
        return n*recur(n-1)

a=int(input(''))
print(recur(a))