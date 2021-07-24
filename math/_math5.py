#백준 1929 

#문제 : M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

#입력 : 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

#출력 : 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

def num_find(a):
    for_return = 1
    if a==1:
        for_return=-1
        return for_return
    for i in range(2,int(a**0.5)+1,1):
        if a%i ==0:
            for_return=-1
            return for_return
    return for_return

M,N= map(int,input("").split(" "))

for i in range(M,N+1):
    if num_find(i)==1:
        print(i)