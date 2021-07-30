import copy

N,M=map(int,input("").split(" "))


list1=list(map(int,input("").split(" ")))#리스트를 받음
list1=sorted(list1)

list2=[[str(k)] for k in list1]
for i in range(M-1):
    New_list=[]
    for k in list2:
        for j in list1:
            if str(j) >= k[-1]:
                New_list.append(k+[str(j)])
    list2=copy.deepcopy(New_list)
count=0
for word in list2:
    for k in word:
        print(k,end=' ')
    count+=1
    print()
