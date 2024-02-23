import sys
sys.setrecursionlimit(10000)


di=[1,-1,0,0,1,1,-1,-1]
dj=[0,0,1,-1,1,-1,1,-1]

def dfs(i,j):
    island[i][j]=0

    for k in range(8):
        ni=i+di[k]
        nj=j+dj[k]

        if 0<=ni<h and 0<=nj<w and island[ni][nj]==1:
            dfs(ni,nj)



while True:
    w,h=map(int,input().split())

    if w==0 and h==0:
        break
    island=[[]for _ in range(h)]




    for i in range(h):
        island[i]=list(map(int,input().split()))

    cnt=0
    for i in range(h):
        for j in range(w):
             if island[i][j]==1:
                dfs(i,j)
                cnt+=1

    print(cnt)















