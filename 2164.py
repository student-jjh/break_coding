N=int(input(""))

list_of_card=[i for i in range(N,0,-1)]
while len(list_of_card)!=1:
    list_of_card.pop()
    temp=list_of_card.pop()
    list_of_card.insert(0,temp)


print(list_of_card[0])