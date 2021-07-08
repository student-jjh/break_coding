def group_check(_word):
    for_check=[]
    for_check.append(_word[0])
    for i in range(1,len(_word),1):
        if _word[i-1] != _word[i] and _word[i] in for_check:
            return -1
        elif _word[i] not in for_check:
            for_check.append(_word[i])
    return 1 

j=int(input(""))
count=0

for i in range(j):
    _word=input("")
    if group_check(_word)==1:
        count+=1
print(count)