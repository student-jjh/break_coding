def appt(k,n):
    nums = [x for x in range(1, n+1)]
    for j in range(k):
        for i in range(len(nums)-1):
            nums[i+1]=nums[i]+nums[i+1]
    return (nums[-1])

a=int(input(""))

for i in range(a):
    c=int(input(""))
    d=int(input(""))
    print(appt(c,d))
