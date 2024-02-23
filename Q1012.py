# 둘 다 풀어보기
import sys
# input=sys.stdin.readline
sys.setrecursionlimit(10000)

total=int(input())

# 0땅 1지렁이

dy=[1,-1,0,0 ]
dx=[0,0,1,-1]

# 되는 놈만 보내기
def dfs(M,N,y,x):
    # global M,N
    if li[y][x]==0:
        return
    li[y][x]=0

    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<=N-1 and 0<=nx<=M-1 and li[ny][nx]==1:
            dfs(M,N,ny,nx)
    


save=[]

for i in range(total):
    M,N,K=map(int,input().split())
    # M : 가로길이
    # N : 세로길이


    li=[[0 for _ in range(M)]for _ in range(N)]

    for _ in range(K):
        X,Y=map(int,input().split())

        # X : 가로
        # Y : 세로

        li[Y][X]=1



    save.append([M,N,li])

for M,N,li in save:
    cnt=0
    for i in range(N):
        for j in range(M):
            if li[i][j]==1:
                dfs(M,N,i,j)
                cnt+=1




    print(cnt)
    



'''
1
4 4 1
3 3
4 3



'''















