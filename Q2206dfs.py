import sys
sys.setrecursionlimit(10000)

# dfs로 했지만 시간 초과.
# 최단 거리는 bfs로 풀 것.

N,M=map(int,input().split())
# N : 줄
# M : 숫자 개수

mymap=[[]for _ in range(N)]

dn=[1,-1,0,0]
dm=[0,0,1,-1]


for i in range(N):
    mymap[i]=list(map(int,input()))



save=[]

def dfs(n,m,cnt,oneflag):


    cnt+=1
    
    mymap[n][m]=cnt

    if n==N-1 and m==M-1:
        save.append(mymap[n][m])

    for i in range(4):
        nn=n+dn[i]
        nm=m+dm[i]
        
        if 0<=nn<N and 0<=nm<M:
            if mymap[nn][nm]==0:
                dfs(nn,nm,cnt,oneflag)
            
            elif mymap[nn][nm]==1 and oneflag:
                dfs(nn,nm,cnt,False)
            else:
                if mymap[nn][nm]>cnt:
                    dfs(nn,nm,cnt,oneflag)


allcheck=False
    
# check
for i in range(N):
    for j in range(M):
        if mymap[i][j]==0:
            allcheck=True


dfs(0,0,1,True)

if allcheck:
    print(-1)
else:
    print(min(save)-1)









