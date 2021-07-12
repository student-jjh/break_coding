import sys

n = int(sys.stdin.readline())
for_answer=[]
for i in range(n):
    a=int(input(""))
    for_answer[int(sys.stdin.readline())] += 1

for_print=sorted(for_answer)
for i in for_print:
    print(i)