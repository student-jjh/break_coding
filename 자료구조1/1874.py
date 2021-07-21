import sys

n=int(input(""))


def stack(n):
    
    list_of_num=[i for i in range(n,0,-1)]
    stack=[]
    for_print=[]
    what_we_want=[]
    for i in range(n):
        what_we_want.append(int(sys.stdin.readline().rstrip()))
    for input_num in what_we_want:
        if input_num in list_of_num:
            while list_of_num[-1] != input_num and list_of_num != []:
                stack.append(list_of_num.pop())
                for_print.append("+")
        if list_of_num != [] and list_of_num[-1]==input_num:
            stack.append(list_of_num.pop())
            for_print.append("+")
        if stack[-1]==input_num:
            stack.pop()
            for_print.append("-")
        else:
            for_print = "NO"
            break
 
    return for_print
a=stack(n)
if a =='NO':
    print(a)
else:
    for i in a:
        print(i)