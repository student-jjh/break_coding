a=[1,2,3,4,5,6,7,8]
b=[8,7,6,5,4,3,2,1]

temp_line=list(map(int,input().split(" ")))
if temp_line ==a:
    print('ascending')
elif temp_line ==b:
    print('descending')
else:
    print('mixed')

