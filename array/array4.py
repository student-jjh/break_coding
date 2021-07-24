for_answer=[]

for i in range(10):
    num=int(input(""))
    if num%42 not in for_answer:
        for_answer.append(num%42)

print(len(for_answer))