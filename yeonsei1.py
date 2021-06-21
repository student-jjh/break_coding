max_score=[100,100,200,200,300,300,400,400,500]

student_score=list(map(int,input("").split(" ")))


def coffee(max_score,student_score):
    total=0
    for i in range(9):
        if student_score[i]-max_score[i]>0:
            return "hacker"
            
        else:
            total+=student_score[i]

    if total>=100:
        return "draw"
    else:
        return "none"

print(coffee(max_score,student_score))