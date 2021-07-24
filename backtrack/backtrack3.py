import copy

N,M=map(int,input("").split(" "))

list1=[str(i+1) for i in range(N)] #N까지의 숫자로 초기화

for i in range(M-1):
    New_list=[]
    for k in list1:
        for j in range(1,N+1):
                New_list.append(k+str(j))
    list1=copy.deepcopy(New_list)

for word in list1:
    for k in word:
        print(k,end=' ')
    print()
