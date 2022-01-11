A,B,C = map(int,input().split())

first = A*B/C
second = A/B*C

print(int(max(first,second)))