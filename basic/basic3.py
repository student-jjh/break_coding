a=int(input(""))
b=int(input(""))

b2=str(b)

for i in b2[::-1]:
    print(a*int(i))

print(a*b)