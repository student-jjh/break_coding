from itertools import combinations

N=int(input())

list_of_coffee =list(map(int,input("").split(" ")))

def coffee(N,list_of_coffee):
    dic_of_sum={}
    for j in range(1,N+1):
        temp_list=list((combinations(list_of_coffee,j)))
        print(temp_list)
        for lista in temp_list:
            dic_of_sum[sum(lista)]=True
    for i in range(1,10000):
        if i not in dic_of_sum:
            return i

print(coffee(N,list_of_coffee))
    