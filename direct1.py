def fibo(n):
    a=[0,1]
    for i in range(2,n+1,1):
        a.append(a[i-1]+a[i-2])
    return a

for_answer=fibo(40)

T=int(input(""))
for i in range(T):
    _num=int(input(""))

    if _num==0:
        print(1,end=" ")
        print(0)
    else:
        print(for_answer[_num-1],end=" ")
        print(for_answer[_num])