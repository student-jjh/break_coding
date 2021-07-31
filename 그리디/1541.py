n=input()
n_list=n.split("-")
for_cal_list=[]
print(n_list)
for i in n_list:
    i_cal=i.split("+")
    total=0
    for j in i_cal:
        if j[0]=="0" and len(j) !=0:
            total+=int(j[1:])
        else:
            total+=int(j)
    for_cal_list.append(total)
    print(for_cal_list)
_total=for_cal_list[0]
if len(n_list) !=1:
    for i in for_cal_list[1:]:
        _total-=i

print(_total)