n=int(input(""))
for_answer=[]
for i in range(n):
    a,b=map(int,input("").split(" "))
    for_answer.append(a+b)

for i in for_answer:
    print(i)
