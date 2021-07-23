import sys
pipe= sys.stdin.readline().rstrip()
pipe_list=pipe.split("()")
total_count=0
now_count=0
for i in pipe_list:
    
    for j in i:
        if j=="(":
            now_count+=1
            total_count+=1
        elif j==")":
            now_count-=1
    total_count+=now_count
    
print(total_count)
