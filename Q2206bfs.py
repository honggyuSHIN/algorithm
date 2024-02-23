from collections import deque
import copy
import sys

input=sys.stdin.readline



N,M=map(int,input().split())
# N : 세로 M : 가로

table=[]

for _ in range(N):
    table.append (list(map(int,input().strip())))




dn=[1,-1,0,0]
dm=[0,0,1,-1]
q=deque()

def bfs(a,b,cnt):
    # 세로 n, 가로 m 좌표   (0,0)
    
    q.append((a,b,cnt))

    while q:
        n,m,cnt=q.popleft()
        cnt+=1

        if n==N-1 and m==M-1:
            return cnt

        for i in range(4):
            dy=n+dn[i]
            dx=m+dm[i]
            if 0<=dy<N and 0<=dx<M:
                if sectable[dy][dx]==0:
                    q.append((dy,dx,cnt))

                    sectable[dy][dx]=cnt






one=set()
mincnt=1000000
for i in range(N):
    for j in range(M):
        if table[i][j]==1:
            one.add((i,j))

for k,l in one:
    sectable=copy.deepcopy(table)
    sectable[k][l]=0
    

    sub=str(bfs(0,0,0))

    if sub=='None':
        continue
    else:
        if mincnt>int(sub):
            mincnt=int(sub)


if mincnt==1000000:
    print(-1)
else:
    print(mincnt)   













'''

벽이 한개도 없는 경우가 존재합니다...

이 경우를 고려하지 않으시면 틀렸습니다가 뜰거에요

저같은 경우는 0,0과 도착점에서 BFS를 두번 실행해서 각 벽까지의 최솟값을 구하는 방식으로 구현했는데

벽이 한개도 없는 경우에 -1을 출력하는거 때문에 애먹었습니다

1
1 1
2
0
3
​
4
answer : 1
5
output : -1

'''