N=int(input(""))
N_list=list(map(int,input().split(" ")))

if len(N_list)==1:
    print("A")
elif len(N_list)==2:
    if N_list[0]==N_list[1]:
        print(N_list[0])
    else:
        print("A")
else:
    a=(N_list[2]-N_list[1])/(N_list[1]-N_list[0])
    if a !=int(a):
        print('B')
    else:
        b=N_list[1]-a*N_list[0]
        print(N_list[-1]*a+b)