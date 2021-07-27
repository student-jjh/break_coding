N=int(input(""))
lista=[]
dica={}
for i in range(N):
    num=int(input(""))
    lista.append(i)
    if i not in dica:
        dica[i]=1
    else:
        dica[i]+=1

for_answer=sorted(lista)

print(sum(round(lista/len(lista)))) #산술평균
print(lista[int(len(lista)/2)])     #중앙값
sorted(dica.items(), key=lambda x: x[1])
print(lista[-1]-lista[0])           #범위