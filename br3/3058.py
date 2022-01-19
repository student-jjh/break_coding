T = int(input())

for i in range(T):
    temp_list = []
    temp_input = list(map(int,input().split()))
    for i in temp_input:
        if i %2 ==0:
            temp_list.append(i)
    temp_list.sort()
    print("{0} {1}".format(sum(temp_list),temp_list[0]))