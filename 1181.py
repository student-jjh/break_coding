N=int(input(""))
list_of_word=[]
for i in range(N):
    temp_word=input("")
    list_of_word.append(temp_word)
list_of_word=list(set(list_of_word))
list_of_word=sorted(list_of_word)
list_of_word.sort(key= lambda x:len(x))

for i in list_of_word:
    print(i)