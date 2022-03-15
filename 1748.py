N = input()
answer = 0
input_N = int(N)
start = 1
end=9
for i in range(1,len(N)+1):
    if end > input_N:
        end = input_N

    answer += (end-start+1) * i
    start = start *10
    end = start * 10 -1

print(answer)