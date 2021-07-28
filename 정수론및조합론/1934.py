def gcd(a,b):

    for i in range(min(a,b),0,-1):
        if a % i ==0 and b % i ==0:
            return i


n=int(input(""))
for i in range(n):
    a,b=map(int,input("").split(" "))
    print(int(a*b/gcd(a,b)))