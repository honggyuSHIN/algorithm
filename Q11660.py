import sys

input=sys.stdin.readline

N,M=map(int,input().split())

table=[]

for _ in range(N):
    table.append(list(map(int,input().split())))


D=[[0 for _ in range(N)]for _ in range(N)]
D[0][0]=table[0][0]

D2=[[0 for _ in range(N)] for _ in range(N)]



for i in range(N):
    for j in range(N):
        if j==0:
            D[i][j]=table[i][j]
        else:
            D[i][j]=D[i][j-1]+table[i][j]

for i in range(N):
    for j in range(N):
        if i==0:
            D2[i][j]=D[i][j]
        else:
            D2[i][j]=D[i][j]+D2[i-1][j]



for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    # x 세로 y 가로
    if x1==1 and y1==1:
        print(D2[x2-1][y2-1])
    elif x1==1:
        print(D2[x2-1][y2-1]-D2[x2-1][y1-2])
    elif y1==1:
        print(D2[x2-1][y2-1]-D2[x1-2][y2-1])
    else:
        print(D2[x2-1][y2-1]-D2[x2-1][y1-2]-D2[x1-2][y2-1]+D2[x1-2][y1-2])



