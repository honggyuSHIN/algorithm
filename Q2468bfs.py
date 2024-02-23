from collections import deque
import sys
import copy

input=sys.stdin.readline
sys.setrecursionlimit(10000)

N=int(input())

ground=[[]for _ in range(N)]

for i in range(N):
    ground[i]=list(map(int,input().split()))

numsave=[]

for i in range(N):
    for j in range(N):
        numsave.append(ground[i][j])

numsave=list(set(numsave))


dn=[1,-1,0,0]
dm=[0,0,1,-1]


q=deque()

def bfs(i,j):
    secondground[i][j]=0

    q.append((i,j))

    # 범위 퍼뜨리기만 하면 됨.
    while q:
        i,j=q.popleft()
        for k in range(4):
            ni=i+dn[k]
            nj=j+dm[k]
            if 0<=ni<N and 0<=nj<N and secondground[ni][nj]!=0:
                secondground[ni][nj]=0
                q.append((ni,nj))


maxcnt=0


for h in numsave:
    cnt=0
    secondground=copy.deepcopy(ground)
    # secondground = [row[:] for row in ground]

    # h 는 높이.

    # 침수시키기
    for i in range(N):
        for j in range(N):
            if secondground[i][j]<=h:
                secondground[i][j]=0

    


    # 구역 개수 확인하기.
    for i in range(N):
        for j in range(N):
            if secondground[i][j]!=0:
                bfs(i,j)
                cnt+=1
                if maxcnt<cnt:
                    maxcnt=cnt


if maxcnt==0:
    print(1)
else:
    print(maxcnt)



