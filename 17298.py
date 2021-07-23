N=int(input(""))
list_of_word=list(map(int,input().split(" ")))
count_dic={}
for i in list_of_word:
    if i not in count_dic:
        count_dic[i]=1
    else:
        count_dic[i]+=1
count_list=[]
for j in list_of_word:
    count_list.append(count_dic[j])
for_return=[-1 for i in range(N)]
not_find=[]
not_find.append(0)

i=1
while not_find and i<N:
    while not_find and count_list[not_find[-1]]<count_list[i]:
        for_return[not_find.pop()]=list_of_word[i]
    not_find.append(i)
    i+=1

for i in for_return:
    print(i,end=" ")