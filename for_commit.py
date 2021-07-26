n=int(input(""))
list_to_find=sorted(list(map(int,input("").split(" "))))
a=int(input(""))
list_for_find=list(map(int,input("").split(" ")))

def bin_search(key,list):
    start=0
    end=len(list)-1
    while True:
        middle=(start+end)//2
        if list[middle]==key:
            return middle
        elif list[middle]<key:
            start=middle+1
        else:
            end=middle-1
        if start>end:
            break
    return -1

for i in list_for_find:
    if bin_search(i,list_to_find)==-1:
        print(0)
    else:
        print(1)