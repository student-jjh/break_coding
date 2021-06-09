import sys

n = input()
n = int(n)

for i in range(0, n):
    x, y = sys.stdin.readline().rsplit()
    x = int(x)
    y = int(y)
    print(x+y)

