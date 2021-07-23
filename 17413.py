def reverse(n):
    for_return=n.split(" ")
    for i in range(len(for_return)):
        for_return[i]=for_return[i][::-1]

    return " ".join(for_return)

S=input("")

for_split_1=[]
for_split_2=[]
for i in range(len(S)):
    if S[i]=='<':
        for_split_1.append(i)
    elif S[i]=='>':
        for_split_2.append(i)
list_of_split=[]
for j in range(len(for_split_1)):
    if j == 0:
        if S[:for_split_1[j]] !="":
            list_of_split.append(S[:for_split_1[j]])
        list_of_split.append(S[for_split_1[j]:for_split_2[j]+1])
    else:
        if S[for_split_2[j-1]+1:for_split_1[j]] !="":
            list_of_split.append(S[for_split_2[j-1]+1:for_split_1[j]])
        list_of_split.append(S[for_split_1[j]:for_split_2[j]+1])

    if j == len(for_split_1)-1 and S[for_split_2[j]+1:]!="":
        list_of_split.append(S[for_split_2[j]+1:])

if list_of_split==[]:
    list_of_split=S.split(" ")


for k in range(len(list_of_split)):
    for_print=list_of_split[k]
    if for_print != "" and for_print[0]!="<":
        for_print=reverse(for_print)
    if k==0:
        print(for_print,end='')
    else:
        if list_of_split[k-1][-1]=='>' or list_of_split[k][0]=='<':
            print(for_print,end="")
        else:
            print(" "+for_print,end="")