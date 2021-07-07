a,b=input("").split(" ")
_a=int(a[::-1])
_b=int(b[::-1])

if _a>=_b:
    print(_a)
else:
    print(_b)