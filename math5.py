def upup(A,B,V):
    if (V-A)%(A-B)==0:
        return int((V-A)/(A-B)+1)
    else:
        return int((V-A)//(A-B)+2)

    

a,b,v=map(int,input("").split(" "))

print(upup(a,b,v))