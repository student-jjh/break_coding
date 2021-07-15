def end_movie(N):
    count=1
    start_num=666
    while count!=N:
        start_num+=1
        if '666' in str(start_num):
            count+=1
        
    print(start_num)

N=int(input(""))
end_movie(N)