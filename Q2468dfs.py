import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
N=int(input())



grounds=[[]for _ in range(N)]

for i in range(N):
    grounds[i]=list(map(int,input().split()))


hlist=[]
for i in range(N):
    for j in range(N):
        hlist.append(grounds[i][j])

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(i,j):
    secondground[i][j]=0

    # 확장하기
    for x in range(4):
        ni=i+dx[x]
        nj=j+dy[x]
        
        if 0<=ni<N and 0<=nj<N and secondground[ni][nj]!=0:
            dfs(ni,nj)






hlist=list(set(hlist))

maxcnt=0




for h in hlist:
    cnt=0
    secondground=[[]for _ in range(N)]
    for i in range(N):
        secondground[i].extend(grounds[i])

    # 물에 잠김    
    for i in range(N):
        for j in range(N):

            if secondground[i][j]<=h:
                secondground[i][j]=0

    
    # 구역 숫자 세기
    for i in range(N):
        for j in range(N):
            if secondground[i][j]!=0:
                dfs(i,j)
                cnt+=1
                if cnt>maxcnt:
                    maxcnt=cnt


if maxcnt==0:
    print(1)
else:
    print(maxcnt)







