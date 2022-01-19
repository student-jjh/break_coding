temp = 0
temp_sum =0

for i in range(1,6):
    temp_list = list(map(int,input().split()))
    if sum(temp_list) > temp_sum:
        temp_sum = sum(temp_list)
        temp = i

print("{0} {1}".format(temp,temp_sum))