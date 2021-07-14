N=input("")
def sum_num(N):
    sum_num=int(N)+sum(int(i) for i in N)
    return sum_num
for i in range(int(N)):
    if sum_num(str(i))==int(N):
        print(i)
        break