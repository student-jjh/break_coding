n=int(input(""))
array1=list(map(int,input("").split(" ")))

max_num=max(array1)
for_answer=[]
for i in array1:
    for_answer.append(i/max_num*100)

print(sum(for_answer)/n)