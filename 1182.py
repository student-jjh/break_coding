from itertools import combinations
N,K = map(int,input("").split(" "))

list_of_coffee =sorted(list(map(int,input("").split(" "))))
def coffee(N,K,list_of_coffee):
    count=0

    for j in range(1,N):
        temp_list=list(combinations(list_of_coffee,j))
        for lista in temp_list:
            if sum(lista) == K:
                count+=1
    return count

print(coffee(N,K,list_of_coffee))