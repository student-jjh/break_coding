T = int(input())

for i in range(T):
    temp_Cent = int(input())
    a = temp_Cent // 25
    b = (temp_Cent % 25) // 10 
    c = ((temp_Cent % 25) % 10) // 5
    d = (((temp_Cent % 25) % 10) % 5)
    print('{0} {1} {2} {3}'.format(a,b,c,d))