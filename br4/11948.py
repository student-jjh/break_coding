temp_list1 = []
temp_list2 = []
for i in range(4):
    temp_list1.append(int(input()))

for i in range(2):
    temp_list2.append(int(input()))

print(sum(temp_list1) - min(temp_list1) + max(temp_list2))