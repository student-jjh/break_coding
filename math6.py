list_pivo=[0,1]

for i in range(2,91,1):
    list_pivo.append(list_pivo[i-1]+list_pivo[i-2])

n=int(input(""))
print(list_pivo[n])
