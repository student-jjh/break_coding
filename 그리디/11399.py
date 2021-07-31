N=int(input(""))
list_of_wait=sorted(list(map(int,input("").split(" "))))
temp=0
total=0
for i in list_of_wait:
    temp=temp+i
    total+=temp
print(total)