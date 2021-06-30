def hotel(H,W,N):
    if N%H==0:
        room_num=H//H
        floor=H
    else:
        room_num=N//H+1
        floor=N-H*(N//H)
    if len(str(room_num))==1:
        return str(floor)+'0'+str(room_num)

    else:
        return str(floor)+str(room_num)


a=int(input(""))
for i in range(a):
    h,w,n=map(int,input("").split(" "))
    print(hotel(h,w,n))