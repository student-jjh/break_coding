N=int(input(""))

list_of_num=[]
dic={}
sum=0
for i in range(N):
    temp_num=int(input(""))
    if temp_num in dic:
        dic[temp_num]+=1
    else:
        dic[temp_num]=1
    list_of_num.append(temp_num)
    sum+=temp_num
dic_keys_list=sorted(dic.keys(),reverse=True)
dic_keys_list=sorted(dic_keys_list,key=lambda x : dic[x])
list_of_num = sorted(list_of_num)
print(round(sum/N))
print(list_of_num[int(N/2)])
if len(dic)>1 and dic[dic_keys_list[-1]]==dic[dic_keys_list[-2]]:
    print(dic_keys_list[-2])
else:
    print(dic_keys_list[-1])
print(list_of_num[-1]-list_of_num[0])