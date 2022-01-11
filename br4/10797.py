Num1 = int(input())

temp_list = list(map(int,input().split()))

count = 0
for num in temp_list:
    if num == Num1:
        count +=1

print(count)