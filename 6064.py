T = int(input())

for i in range(T):
    M,N,x,y = map(int,input().split())
    x-=1
    y-=1
    ok = False
    for j in range(x,M*N,M):
        if j%N == y:
            ok = True
            print(j+1)
            break
    if ok == False:
        print(-1)