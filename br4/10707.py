A = int(input())
B= int(input())
C = int(input())
D = int(input())
P = int(input())

case_1=P*A
if P >C:
    case_2 = (P-C)*D + B
else:
    case_2=B

print(min(case_1,case_2))