import operator
strings=input("").upper()

count={}

for i in strings:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1

sdict=sorted(count.items(),key=operator.itemgetter(1))

if len(count)==1:
    print(sdict[-1][0])
elif sdict[-1][1] == sdict[-2][1]:
    print('?')
else:
    print(sdict[-1][0])

