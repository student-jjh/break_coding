A,B = map(int,input().split())

def gcd(A,B):
    if B == 0:
        return A
    else:
        return gcd(B,A%B)


gcd_a = gcd(A,B)

print(gcd_a)
print(int(A*B/gcd_a))