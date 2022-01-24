N = input()
answer = "NO"
if len(N) !=1:
    for i in range(len(N)):
        temp_front=N[:i]
        temp_end =N[i:]

        temp_front_cal = 1
        temp_end_cal = 1

        for f in temp_front:
            temp_front_cal *= int(f)

        for e in temp_end:
            temp_end_cal *= int(e)
        if temp_front_cal ==temp_end_cal:
            answer = "YES"
print(answer)