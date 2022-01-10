N,M = map(int,input().split())

first = (N//2) * M + (N%2)*(M//2)
second = (M//2) * N + (M%2)*(N//2)
print(max(first,second))