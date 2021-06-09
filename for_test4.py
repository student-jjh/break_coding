import sys

n = input()
n = int(n)

for i in range(0, n):
    x, y = sys.stdin.readline().rsplit()
    x = int(x)
    y = int(y)
    print(x+y)

# 어떤 원리로 작동하는지르 잘 모르겠다고 해야하나 어렵네요 질문이 필요할듯