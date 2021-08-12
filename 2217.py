N=int(input(""))
rope_list=[]
sum_weight=0
for i in range(N):
    temp_rope = int(input(""))
    rope_list.append(temp_rope)
    sum_weight+=temp_rope
rope_list.sort()
max_weight=0
for i in range(len(rope_list)):
    if rope_list[i]*(len(rope_list)-i) >max_weight:
        max_weight=rope_list[i]*(len(rope_list)-i)

print(max_weight)