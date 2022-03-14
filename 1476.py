E,S,M = map(int,input().split())

n = 0

while True:
    if (n % 15 == (E-1) and n % 28 ==(S-1) and n%19 ==(M-1)):
        print(n+1)
        break
    else:
        n+=1