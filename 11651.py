N=int(input(""))
list_of_comma=[]
for i in range(N):
    lista=list(map(int,input("").split(" ")))[::-1]
    list_of_comma.append(lista)
for_print=sorted(list_of_comma)

for i in for_print:
    for j in range(len(i)-1,-1,-1):
        print(i[j],end=' ')
    print()