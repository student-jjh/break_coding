max_num=0
count=0
for i in range(1,10,1):
    nums=int(input(""))
    if nums>=max_num:
        max_num=nums
        count=i

print(max_num)
print(count)