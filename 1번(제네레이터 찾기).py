list_a=list(range(1,5001))

def gen_find(n):
    _num=n+sum(int(x) for x in str(n) )
    return _num

for i in range(1,5001):
    if gen_find(i) in list_a:
        list_a.remove(gen_find(i))
    

print(sum(list_a))

