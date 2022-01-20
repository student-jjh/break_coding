temp_list = list(map(int,input().split()))

temp_list.sort()

temp_num = int(temp_list[2])

while True:
    # print(temp_list)
    count = 0
    for num in temp_list:
        if temp_num % num ==0:
            count+=1
    if count >=3:
        print(temp_num)
        break
    else:
        temp_num+=1