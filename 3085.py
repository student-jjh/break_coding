N= int(input())

board = []


def check(board):
    n=len(board)
    ans = 1
    for i in range(n):
        cnt =1 
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                cnt +=1
            else:
                cnt =1
            if ans < cnt :
                ans = cnt
    for j in range(n):
        cnt = 1
        for i in range(1,n):
            if board[i][j] == board[i-1][j]:
                cnt +=1
            else:
                cnt =1
            if ans<cnt:
                ans =cnt
    return ans


for i in range(N):
    board.append(list(input()))

answer = 1

for i in range(N):
    for j in range(N):
        if i<N-1:
            board[i][j] , board[i+1][j] = board[i+1][j], board[i][j]
            temp = check(board)
            if temp > answer:
                answer = temp
            board[i][j] , board[i+1][j] = board[i+1][j], board[i][j]
        
        if j<N-1:
            board[i][j] , board[i][j+1] = board[i][j+1], board[i][j]
            temp = check(board)
            if temp > answer:
                answer = temp
            board[i][j] , board[i][j+1] = board[i][j+1], board[i][j]


print(answer)