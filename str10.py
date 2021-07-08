cro=['c=','c-','lj','nj','s=','z=']
cro2=['dz=']

for_min=0
word=input("")
i=0
while i<len(word):
    try:
        if word[i:i+3] in cro2:
            for_min+=1
            i+=3
            continue
        elif word[i:i+2] in cro:
            for_min+=1
            i+=2
            continue
    except:
        pass
    for_min+=1
    i+=1

print(for_min)
