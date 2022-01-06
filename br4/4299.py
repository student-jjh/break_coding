a,b = map(int,input().split())
 
temp_list = []
temp_list.append((a+b)//2)
temp_list.append((a-b)//2)
temp_list.sort()
if  a+b < 0 or a-b < 0 or (a + b) % 2:
    print(-1)
else:
    print("{0} {1}".format(temp_list[1],temp_list[0])) 