doing = True

while doing:
    temp_list = list(map(int,input().split()))
    if temp_list == [0]:
        doing = False 
        break 
    temp_br =1

    for i in range(1,len(temp_list)):
        if i%2 == 1:
            temp_br *=temp_list[i]
        else:
            temp_br -=temp_list[i]
    print(temp_br)