
from collections import deque
    
q=deque()


dw=[1,-1,0,0,1,1,-1,-1]
dh=[0,0,1,-1,1,-1,1,-1]

def dfs(i,j):
    island[i][j]=0
    q.append((i,j))

    while q:
        i,j=q.popleft()

        for k in range(8):
            ni=i+dw[k]
            nj=j+dh[k]
            if 0<=ni<h and 0<=nj<w and island[ni][nj]==1:
                island[ni][nj]=0
                q.append((ni,nj))




while True:
    islandcnt=0
    w,h=map(int,input().split())
    # w : 너비 h : 높이

    if w==0 and h==0:
        break

    island=[[]for _ in range(h)]

    for i in range(h):
        island[i]=list(map(int,input().split()))


    for i in range(h):
        for j in range(w):
            if island[i][j]==1:
                dfs(i,j)
                islandcnt+=1
    print(islandcnt)















