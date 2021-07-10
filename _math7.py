x=[]
y=[]
for i in range(3):
    x_append,y_append=map(int,input("").split(" "))
    if x_append in x:
        x.remove(x_append)
    else:
        x.append(x_append)
    if y_append in y:
        y.remove(y_append)
    else:
        y.append(y_append)
print(x[0],end=" ")
print(y[0])


