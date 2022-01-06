burger = []
dirnk = []
for i in range(3):
    temp_b = int(input())
    burger.append(temp_b)
    burger.sort()

for i in range(2):
    temp_b = int(input())
    dirnk.append(temp_b)
    dirnk.sort()

print(burger[0] + dirnk[0] -50)