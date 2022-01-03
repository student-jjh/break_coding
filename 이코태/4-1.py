N=int(input())
moves=input().split()
x=1
y=1
for move in moves:
    if move=='L':
        if x-1>0:
            x-=1
    elif move=='R':
        if x+1<N:
            x+=1
    elif move=='U':
        if y-1>0:
            y-=1
    elif move=='D':
        if y+1<N:
            y+=1
print(y,end=' ')
print(x)