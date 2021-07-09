def num_find(a):
    for_return=1

    if a==1:
        for_return=-1
    for i in range(2,a,1):
        if a%i ==0:
            for_return=-1

    return for_return

k=int(input(""))

lista=list(map(int,input("").split(" ")))
count=0
for j in range(k):
    if num_find(lista[j])==1:
        count+=1

print(count)
