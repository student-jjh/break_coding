N=int(input(""))
list_of_comma=[]
for i in range(N):
    lista=list(map(int,input("").split(" ")))
    list_of_comma.append(lista)
for_print=sorted(list_of_comma)
print(for_print)
#for i in for_print:
#   print(" ".join(i))