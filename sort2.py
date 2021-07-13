N=int(input(""))
for_answer=[]
for i in range(N):
    a=int(input(""))
    for_answer.append(a)
def bubble_sort(lista):
    n=len(lista)
    for i in range(n-1,0,-1):
        for j in range(i,0,-1):
            if lista[j]<lista[j-1]:
                lista[j],lista[j-1]=lista[j-1],lista[j]
    return lista


for_print=bubble_sort(for_answer)
for i in for_print:
    print(i)