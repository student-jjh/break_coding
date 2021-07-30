N=int(input(""))
list_of_comma=[]
for i in range(N):
    lista=list(map(int,input("").split(" ")))
    list_of_comma.append(lista)
for_print=sorted(list_of_comma)

for i in for_print:
    for j in i:
        print(j,end=' ')
    print()