for_answer=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
_count=0
for x in range(0,4,1):
    if for_answer[0][x]==0:
        for_answer[0][x]=_count
        _count+=1

print(for_answer)