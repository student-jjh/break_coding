def winer(x,y):
    x_point,y_point=0,0
    if x[0]>y[0]:
        x_point+=1
    elif x[0]<y[0]:
        y_point+=1

    if x[1]>y[1]:
        x_point+=1
    elif x[1]<y[1]:
        y_point+=1

    if x_point==2:
        return 'y'
    elif y_point==2:
        return 'x'
    else:
        return False

N=int(input(""))
for_answer=[]
for i in range(N):
    person=list(map(int,input("").split(" ")))
    person.append(1)
    if for_answer==[]:
        for_answer.append(person)
    else:
        for j in for_answer:
            if winer(j[:2],person[:2])=='x':
                j[2]+=1
            elif winer(j[:2],person[:2])=='y':
                person[2]+=1
        for_answer.append(person)
for k in for_answer:
    print(k[2],end=' ') 

 