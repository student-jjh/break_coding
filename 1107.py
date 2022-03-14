N = int(input())
M = int(input())

broken = [True]*10
if M !=0:
    temp_list = list(map(int,input().split()))
    for num in temp_list:
        broken[num] = False

def isPossibe(number):
    cnt = 0
    if number == 0:
        return 1
    while number!=0:
        if broken[number%10]:
            cnt +=1
            number = number//10
        else:
            return False
    
    return cnt

answer = abs(100 - N)
for i in range(1000000):
    temp = isPossibe(i)
    if temp:
        if temp + abs(i - N) < answer:
            answer = temp + abs(i-N)

print(answer)