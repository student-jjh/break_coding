def ara(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return a

def min_set(lists):
    min=10000
    min_num=0
    for i in lists:
        if abs(i[1]-i[0])<min:
            min=abs(i[1]-i[0])
            min_num=i
    return min_num

for_answer_array=ara(10000)

T=int(input(""))
for i in range(T):
    for_print=[]
    n=int(input(""))
    for j in range(int(n/2)+1):
        if for_answer_array[j] and for_answer_array[n-j]:
            for_print.append((j,n-j))

    for i in min_set(for_print):
        print(i,end=' ')
    print("")