#분수찾기 
for_list=[]
n=1
while n*(n+1)/2<=10000000:
   for_list.append(n*(n+1)/2)
   n+=1
for_list.append(10000000)
_num=int(input(""))
for i in range(len(for_list)):
    if for_list[i]>=_num:
        a=int(_num-for_list[i-1])
        b=int(i-a+2)
        print(str(b)+"/"+str(a))
        break
