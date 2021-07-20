def star(N):
    for i in range(N,0,-1):
        print((N-i)*" "+(i)*'*')

N=int(input(""))
star(N)