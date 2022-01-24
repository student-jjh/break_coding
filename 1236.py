N,M = map(int,input().split())
temp_list =  []
for i in range(N):
    temp_list.append(input())
print(temp_list)
forjcheck = [0 in range (M)]
foricheck = [0 in range (N)]
for i in range(N):
    for j in range(M):
        if temp_list[i][j] == 'X':
            print(foricheck)
            print(forjcheck)
            foricheck[i] =1
            forjcheck[j] =1
print((M+N - sum(foricheck) -sum(forjcheck))//2)