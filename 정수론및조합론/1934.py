import sys
def for_print(a,b):
    i=2
    for_cal=[]
    while i <= a and i<=b:
        plus=True
        if a%i ==0:
            plus=False
            a=a//i
        if b%i==0:
            plus=False
            b=b//i
        if plus:
            i+=1
        else:
            for_cal.append(i)

    for_cal.append(a)
    for_cal.append(b)
    answer=1
    for i in for_cal:
        answer*=i
    print(answer)
n=int(input(""))
for i in range(n):
    a,b=map(int,sys.stdin.readline().rstrip().split(" "))
    for_print(a,b)
