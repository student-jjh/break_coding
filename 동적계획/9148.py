dic={}
def w(a,b,c):
    if (a,b,c) in dic:
        return dic[(a,b,c)]
    elif a <= 0 or b <= 0 or c <= 0:
        dic[(a, b, c)]=1 
        return 1

    elif a > 20 or b > 20 or c > 20:
        dic[(a,b,c)]=w(20,20,20)
        return dic[(a,b,c)]

    elif a < b and b < c:
        dic[(a,b,c)]=w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dic[(a,b,c)]
    else:
        dic[(a,b,c)]=w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return dic[(a,b,c)]
    
while True:
    a,b,c=map(int,input("").split(" "))
    if (a,b,c)==(-1,-1,-1):
        break
    print("w({0}, {1}, {2}) = {3}".format(a,b,c,w(a,b,c)))
