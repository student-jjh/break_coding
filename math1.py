def money(a,b,c):
    if c<=b:
        print(-1)
    elif a/(c-b)==int(a/(c-b)):
        print(int(a/(c-b))+1)
    else:
        print(int(a/(c-b))+1)

a,b,c=map(int,input("").split(" "))

money(a,b,c)

