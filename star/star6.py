def star(N):
    for i in range(1,N+1,1):
        print(i*'*'+(N-i)*2*" "+i*'*')

    for i in range(N-1,0,-1):
        print(i*'*'+(N-i)*2*" "+i*'*')

N=int(input(""))
star(N)