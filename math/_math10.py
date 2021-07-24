T=int(input(""))
def long(x1,y1,x2,y2):
    return ((x2-x1)**2 +(y2-y1)**2)**0.5
for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input("").split(" "))
    if r1 >=r2:
        _long=r1
        _short=r2
    else:
        _long=r2
        _short=r1
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif (long(x1,y1,x2,y2))+_short==_long or _short+_long == long(x1,y1,x2,y2):
        print(1)
    elif _long-_short<long(x1,y1,x2,y2) and _long+_short > long(x1,y1,x2,y2):
        print(2)
    else:
        print(0)