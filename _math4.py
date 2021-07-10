#백준 11653번 

#정수 N이 주어졌을 때, 소인수 분해하는 프로그램을 작성

def answer(N):
    start=2
    for_print=[]
    while N>1:
        if N % start ==0:
            for_print.append(start)
            N=N//start
        else:
            start+=1

    return for_print

N=int(input())

for i in answer(N):
    print(i)