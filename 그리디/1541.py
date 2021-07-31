n=input()
n_list=n.split("-")
for i in range(len(n_list)):
    exec('n_list[i]='+n_list[i])
total=n_list[0]
if len(n_list) !=1:
    for i in n_list[1:]:
        total-=i

print(total)