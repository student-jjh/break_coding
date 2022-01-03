answer = [1,1,2,2,2,8]

temp_list = list(map(int,input().split()))

for_answer = []
for i in range(len(answer)):
    print(answer[i] - temp_list[i],end=' ')
