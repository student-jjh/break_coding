a,b=map(int,input('').split(' '))
for_answer=array = [[0 for col in range(a)] for row in range(b)]

print(for_answer)
_count=1
max_count=a*b
min_x=0
min_y=0

max_x=a
max_y=b


def print_x(x):
    for i in range(len(x)):
        print(x[i])
while _count<=max_count:
    for x in range(min_x,max_x,1):
        if for_answer[min_y][x]==0:
            for_answer[min_y][x]=_count
            _count+=1
    min_y+=1
    print(1)
    for y in range(min_y,max_y,1):
        if for_answer[y][max_x-1] ==0:
            for_answer[y][max_x-1]=_count
            _count+=1
    max_x-=1
    print(2)
    for x in range(max_x-1,min_x-1,-1):
        if for_answer[max_y-1][x]==0:
            for_answer[max_y-1][x]=_count
            _count+=1
    max_y-=1
    print(3)
    for y in range(max_y-1,min_y-1,-1):
        if for_answer[y][min_x]==0:
            for_answer[y][min_x]=_count
            _count+=1
    min_x+=1



print_x(for_answer)


