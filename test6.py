import copy 
a=[1,2,3]
b=copy.copy(a)
a[2]=1
print(a)
print(b)