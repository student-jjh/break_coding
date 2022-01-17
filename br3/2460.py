start =0
max = 0
for i in range(10):
    temp_min,tmep_plus = map(int,input().split())
    start -=temp_min
    start +=tmep_plus
    if start >max:
        max = start
print(max)