a=int(input(""))
b=int(input(""))
c=int(input(""))

abc=str(a*b*c)

for i in range(10):
    count=0
    for j in abc:
        if j==str(i):
            count+=1
    print(count) 

