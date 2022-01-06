L= int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A%C ==0:
    first = A//C
else:
    first = A//C +1

if B%D ==0:
    second = B//D
else:
    second = B//D +1

day = max(first,second)

print(L-day)