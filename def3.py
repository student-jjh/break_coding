def nums(a):
    count=0
    for i in range(1,a+1,1):
        for_answer=[]
        if len(str(i))<=2:
            count+=1
        else:
            for j in range(len(str(i))-1):
                if int(str(i)[j+1])-int(str(i)[j]) not in for_answer:
                    for_answer.append(int(str(i)[j+1])-int(str(i)[j]))
            if len(for_answer)==1:
                count+=1    
    return count
a=int(input(""))

print(nums(a))