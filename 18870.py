N=int(input())
list_for_input=list(map(int,input("").split(" ")))
list_for_check=sorted(list(set(list_for_input)))
list_for_answer=[]

dic={}
for num in range(N):
    if list_for_input[num] in dic:
        list_for_answer.append(dic[list_for_input[num]])
    else:
        count=len(list_for_check[:list_for_check.index(list_for_input[num])])
        dic[list_for_input[num]]=count
        list_for_answer.append(count)
for v in list_for_answer:
    print(v,end=" ") 