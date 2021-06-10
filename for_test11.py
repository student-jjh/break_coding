a,b=map(int,input("").split(" "))
for_answer=[]

list_a=list(map(int,input("").split(" ")))

for i in list_a:
    if i<b:
        for_answer.append(i)

for j in for_answer:
    print(j,end=' ')

