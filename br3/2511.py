tmepA = list(map(int,input().split()))
tmepB = list(map(int,input().split()))
score_A =0
score_B =0
win = 0
for i in range(10):
    if tmepA[i]>tmepB[i]:
        score_A +=3
        win = 'A'
    elif tmepA[i]<tmepB[i]:
        score_B +=3
        win = 'B'
    else:
        score_B +=1
        score_A +=1
        win = 'D'
print("{0} {1}".format(score_A,score_B))
if score_A > score_B:
    print("A")
elif score_B > score_A:
    print('B')
else:
    print(win)