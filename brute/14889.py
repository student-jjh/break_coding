from itertools import combinations
N=int(input())

list_of_num=[i for i in range(N)]

list_of_con=list(combinations(list_of_num,N//2))

list_of_power=[]
total_power=0

for j in range(N):
    list_of_power.append(list(map(int,input().split(" "))))
min_power=10000
for n in range(len(list_of_con)//2):
    temps_list=list_of_con[n]
    lest_list=list_of_con[-n-1]
    lest_power=0
    temp_power=0
    for i in range(N//2):
        for j in range(N//2):
            lest_power+=list_of_power[lest_list[i]][lest_list[j]] +list_of_power[lest_list[j]][lest_list[j]]
            temp_power+=list_of_power[temps_list[i]][temps_list[j]] +list_of_power[temps_list[j]][temps_list[j]]
    if abs(lest_power-temp_power)<min_power:
        min_power = abs(lest_power-temp_power)

print(min_power)