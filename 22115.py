from itertools import combinations
N,K = map(int,input("").split(" "))

list_of_coffee =sorted(list(map(int,input("").split(" "))))
def coffee(N,K,list_of_coffee):

    for i in range(N):
        if sum(list_of_coffee[-1-i:]) >=K:
            break
    for j in range(i+1,N,1):
        temp_list=list(set(combinations(list_of_coffee,j)))
        for lista in temp_list:
            if sum(lista) == K:
                return j
    return -1

print(coffee(N,K,list_of_coffee))