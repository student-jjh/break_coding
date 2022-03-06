MAX = 1000000
F = [1]*(MAX+1)
G = [0]*(MAX+1)

for i in range(2,MAX+1):
    j =1 
    while i*j <= MAX:
        F[i*j] += i
        j+=1

for k in range(1,MAX+1):
    G[k] = G[k-1] + F[k]


T = int(input())
ans = []
for i in range(T):
    N = int(input())
    ans.append(G[N])

print('\n'.join(map(str,ans))+'\n')

# test Case 문제의 경우 전부 답을 우선 다 구해두는 방법도 생각해 보는 것을 습관화 하자
# 복습 하고 이러한 문제의 경우 많은 경우 다른 접근방법이 있을 수 있는 것이 아닌 거의 정답이 정해져 있는 느낌이니 복습해두자