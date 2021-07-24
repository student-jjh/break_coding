import copy

def plusnum(n):
    start_a=-1
    count=0
    for_answer=copy.deepcopy(n)
    while start_a != n:
        left=str(for_answer%10)
        right=str(sum([int(i) for i in str(for_answer)])%10)

        start_a=int(left+right)
        for_answer=copy.deepcopy(start_a)
        count+=1
    return count

num=int(input(""))

print(plusnum(num))