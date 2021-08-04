N=int(input(""))
list_of_player=[]

for i in range(N):
    age,name=input("").split(" ")
    age=int(age)
    list_of_player.append((age,name))

list_of_player.sort(key=lambda x:x[0])

for i in list_of_player:
    print(i[0],end=" ")
    print(i[1])