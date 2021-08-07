import copy
list_of_num=['0','1','2','3','4','5','6','7','8','9']
list_of_answer=['0','1','2','3','4','5','6','7','8','9']
k=int(input(""))
list_of_cal=input("").split(" ")
for cal in list_of_cal:
    temp_list=[]
    for front_num in list_of_answer:
        for back_num in list_of_num:
            if back_num not in front_num:
                exec('temp='+front_num[-1]+cal+back_num)
                if temp:
                    temp_list.append(front_num+back_num)
    list_of_answer=copy.copy(temp_list)


print(list_of_answer[-1])
print(list_of_answer[0])