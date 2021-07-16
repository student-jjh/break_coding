white_start=['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
black_start=['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']

N,M=map(int,input("").split(" "))
board=[]
for i in range(N):
    board.append(input(""))
min=64
for i in range(N-7):
    for j in range(M-7):
        white_wrong=0
        black_wrong=0
        compar_area=board[:i+8]
        for k in compar_area:
            compar_line=k[j:j+8]
            for i in range(8):
                pass
