def fac(N):
    for_return=1
    for i in range(1,N+1):
        for_return*=i
    return str(for_return)

def zeroCount(strs):
    count=0
    for i in range(len(strs)-1,0,-1):
        if strs[i] == "0":
            count+=1
        else:
            return count
    return count

N=int(input())
print(fac(10))
print(zeroCount(fac(N)))