N=int(input(""))
list_of_word=list(map(int,input().split(" ")))
for_return=[-1 for i in range(N)]
not_find=[]
not_find.append(0)
i=1
while not_find and i<N:
    while not_find and list_of_word[not_find[-1]]<list_of_word[i]:
        for_return[not_find.pop()]=list_of_word[i]
    not_find.append(i)
    i+=1

for i in for_return:
    print(i,end=" ")