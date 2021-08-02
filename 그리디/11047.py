N,K=map(int,input("").split(" "))
list_of_coin=[]

for i in range(N):
    a=int(input(""))
    list_of_coin.append(a)
count=0
for coin in list_of_coin[::-1]:
    if K>=coin:
        count+=K//coin
        K=K%coin

print(count)
