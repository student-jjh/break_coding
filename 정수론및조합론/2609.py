a,b=map(int,input("").split(" "))
for i in range(min(a,b),0,-1):
    if a % i ==0 and b % i ==0:
         print(i)
         break
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
    #print(i)
    #print(for_cal)
    #print(a)
    #print(b)
for_cal.append(a)
for_cal.append(b)
answer=1
for i in for_cal:
    answer*=i
print(answer)