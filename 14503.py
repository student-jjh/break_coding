N,M=map(int,input().split())
r,c,d=map(int,input().split())
clean_map=[]
for i in range(N):
    temp_map=list(map(int,input().split()))
    clean_map.append(temp_map)
print(clean_map)