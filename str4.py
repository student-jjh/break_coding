nums=int(input(""))

for i in range(nums):
    a,b=input("").split(" ")
    for k in b:
       print(k*int(a),end='')
    print("")
    