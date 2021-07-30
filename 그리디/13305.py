N=int(input(""))
list_of_long=list(map(int,input().split()))
list_of_money=list(map(int,input().split()))
min=list_of_money[0]
distence=0
total_fee=0
for i in range(len(list_of_money)-1):
    if list_of_money[i]>=min:
        distence+=list_of_long[i]
    else:
        total_fee+=distence*min
        min=list_of_money[i]
        distence=list_of_long[i]
total_fee+=min*distence
print(total_fee)
