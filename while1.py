bool_a=True

while bool_a:
    a,b=map(int,input().split(" "))

    if a==0 and b==0:
        bool_a=False
    else:
        print(a+b)