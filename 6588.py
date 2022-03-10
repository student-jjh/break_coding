

prime = []
num = [False] * 1000000 

for i in range(2,1000000):
    if num[i] == False:
        prime.append(i)
        for k in range(i+i,1000000,i):
            num[k] = True



while True:
    N = int(input())
    if N == 0:
        break
    for nums in prime:
        if num[N-nums] == False:
            print("{0} = {1} + {2}".format(N,nums,N-nums))
            break