num=0
for i in range(5):
    num+=int(input(""))
    if num>40:
        num+=int(input(""))
    else:
        num+=40

print(int(num/5))
