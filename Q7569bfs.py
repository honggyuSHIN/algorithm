from collections import deque
import sys
sys.setrecursionlimit(10000)

M,N,H=map(int,input().split())
# M : 가로  N : 세로    H : 높이
# N - H - M 순서로 접근.

table=[[[]for _ in range(N)]for _ in range(H)]


for i in range(H):
    for j in range(N):
        table[i][j]=list(map(int,input().split()))



q=deque()



dm=[1,-1,0,0,0,0]
dn=[0,0,1,-1,0,0]
dh=[0,0,0,0,1,-1]


for i in range(H):
    for j in range(N):
        for k in range(M):
            if table[i][j][k]==1:
                q.append((i,j,k,1))

maxcnt=0
def bfs():
    global maxcnt
    # 바꾸기


    
    # 전염만
    while q:
        h,n,m,cnt=q.popleft()
        cnt+=1

        for i in range(6):
            nn=n+dn[i]
            nm=m+dm[i]
            nh=h+dh[i]
            if 0<=nn<N:
                if 0<=nm<M:
                    if 0<=nh<H:
                        if table[nh][nn][nm]==0:
                            table[nh][nn][nm]=cnt
                            q.append((nh,nn,nm,cnt))
                    

cnt=1
bfs()





flag=False

for i in range(H):
    for j in range(N):
        for k in range(M):
            if table[i][j][k]==0:
                flag=True
            if table[i][j][k]>maxcnt:
                maxcnt=table[i][j][k]



if flag:
    print(-1)
else:
    print(maxcnt-1)















