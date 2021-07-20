
def triple(base):
    num=len(base.split("\n")[0])
    bases=base.split("\n")
    first="\n".join([i+i+i for i in bases])
    second="\n".join([i+" "*num+i for i in bases])
    third="\n".join([i+i+i for i in bases]) 
    total=first+"\n"+second+"\n"+third

    return total

def star(N):
    base='***\n* *\n***'
    while N>3:
        base=triple(base)
        N=int(N/3)
    return base
N=int(input(""))

print(star(N))