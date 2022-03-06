
while True:
    try:
        N = int(input())
        a=1
        temp = 1

        while True:
            if (temp % N ==0):
                break
            else :
                temp = (temp%N) * 10 +1
                a+=1

        print(a)

    except:
        break
