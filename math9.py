import math
a=int(input(""))

for i in range(a):
    c,d=map(int,input("").split(" "))
    dis=d-c

    for_sqrt=math.floor(math.sqrt(dis))
    _sqrt=for_sqrt**2
    sqrt=math.sqrt(_sqrt)
    for_print=0

    
    if dis > _sqrt+sqrt:
        
        for_print=for_sqrt*2+1
    elif dis<_sqrt+sqrt and dis>_sqrt:

        for_print=for_sqrt*2    
    elif dis == _sqrt:
   
        for_print=for_sqrt*2-1
   
    if dis<=3:
        for_print=dis

    print(for_print)
    print(for_sqrt)
    print(sqrt)