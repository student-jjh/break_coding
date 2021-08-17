from itertools import combinations
list_of_person=[]
for i in range(9):
    temp_person=int(input())
    list_of_person.append(temp_person)

possible=list(combinations(list_of_person,7))

for tuples in possible:
    if sum(tuples)==100:
        break
for person in sorted(list(tuples)):
    print(person)
