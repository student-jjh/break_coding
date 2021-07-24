N,M=map(int,input("").split(" "))
blackjack_list=list(map(int,input("").split(" ")))
best_num=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if M-(blackjack_list[i]+blackjack_list[j]+blackjack_list[k])>=0 and M-best_num>M-(blackjack_list[i]+blackjack_list[j]+blackjack_list[k]):
                best_num=(blackjack_list[i]+blackjack_list[j]+blackjack_list[k])

print(best_num)
