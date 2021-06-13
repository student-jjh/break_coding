#벌집문제
for_list=[]
n=0
while 3*n*(n+1)<=1000000000:
   for_list.append(3*n*(n+1)+1)
   n+=1
for_list.append(1000000000)
_num=int(input(""))
for i in range(len(for_list)):
    if for_list[i]>=_num:
        print(i+1)
        break
