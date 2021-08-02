import copy
#가장 일찍 끝나는 회의를 찾는다
#그 끝나는 타임보다 먼저 시작하는 강의들을 리스트업하고 다시 ㄱ
#리스트업된 강의가 없을 때 까지 while 문을 돌리면 해결되지 않을까..? 

N=int(input(""))
done_list=[]

ready_list=[]
for i in range(N):
    temp_list=list(map(int,input("").split(" ")))[::-1]
    ready_list.append(temp_list)
ready_list=sorted(ready_list)
count=0
while ready_list !=[]:
    min=ready_list[0][0]
    min_list=ready_list[0]
    for_copy=[]
    done_list.append(min_list)
    count+=1
    for j in ready_list:
        if j[1]>=min_list[0]:
            for_copy.append(j)
    ready_list=copy.copy(for_copy)
print(count)