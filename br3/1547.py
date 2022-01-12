M = int(input())
now = 1
for  i in range(M):
    temp_list = list(map(int,input().split()))
    if now in temp_list:
        if temp_list[0] == now:
            now = temp_list[1]
        else:
            now= temp_list[0]

print(now)