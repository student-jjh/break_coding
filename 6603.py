from itertools import combinations
while True:
    temp=input("")
    if temp == '0':
        break
    else:
        temp_list=temp.split(" ")[1:]
    temp_com =list(combinations(temp_list,6))
    for lists in temp_com:
        tempstr=" ".join(lists)
        print(tempstr)
    print()
