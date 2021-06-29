C=int(input(""))
for i in range(C):
    count=0
    arrays=list(map(int,input('').split(' ')))
    aves=sum(arrays[1:])/arrays[0]
    for i in arrays[1:]:
        if i > aves:
            count+=1
    print("{:.3f}".format((count/arrays[0]*100))+'%')