def appt(k,n):
    if n==1:
        return 1
    elif k==0:
        return n
 
    
    else:
        return appt(k-1,n)+appt(k,n-1)

'''
a=int(input(""))

lista=[]
for i in range(a*2):
    lista.append(int(input("")))

for i in range(0,a+1,2):
    print(appt(lista[i],lista[i+1]))
    '''

print(appt(14,14))