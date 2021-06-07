import copy
def hide_seek(start,end):
    new_list=[start]
    count=0
    while end not in new_list:
        was_list=copy.deepcopy(new_list)
        new_list=[]
        for i in was_list:

            new_list.append(i+1)
            new_list.append(i-1)
            new_list.append(i*2)
        count+=1
        new_set=set(new_list)
        new_list=list(new_set)
    return count
        

if __name__=="__main__":
    start,end=map(int,input("").split(" "))
    print(hide_seek(start,end))