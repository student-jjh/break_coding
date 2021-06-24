def nums(a):
    count=0
    for i in range(1,a+1,1):
        if len(str(i))<=2:
            count+=1
        else:
            for j in range(len(str(a))):
                
