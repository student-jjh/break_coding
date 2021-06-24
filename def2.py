for_answer=[i for i in range(10001)]
for_min=[]
def self_num(a):
    return a+sum(int(i) for i in str(a))

for i in range(0,10001,1):
    if self_num(i) in for_answer:
        for_answer.remove(self_num(i))

print(for_answer)