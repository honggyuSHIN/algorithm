
from collections import deque
import sys

input=sys.stdin.readline

N,M=map(int,input().split())
# N : 세로 M : 가로

table=[]

for _ in range(N):
    table.append(list(map(int,input().strip())))


q=deque()

q.append((0,0,0,0))


dn=[1,-1,0,0]
dm=[0,0,1,-1]

flag=False
secondflag=False
while q:
    n,m,cnt,visited=q.popleft()
    

    if n==N-1 and m==M-1:

        flag=True
        break
    cnt+=1
    for i in range(4):
        nn=n+dn[i]
        nm=m+dm[i]

        if 0<=nn<N and 0<=nm<M:
            if table[nn][nm]==0:
                table[nn][nm]=[cnt,visited]
                q.append((nn,nm,cnt,visited))
            elif table[nn][nm]==1:
                if visited==0:
                    table[nn][nm]=[cnt,visited]
                    q.append((nn,nm,cnt,1))
            else:
                if visited==0:
                    if table[nn][nm][1]==1:
                        table[nn][nm]=(cnt,visited)
                        q.append((nn,nm,cnt,visited))


if flag:
    try:
        print(table[N-1][M-1][0]+1)
    except:
        print(table[N-1][M-1]+1)
else:
    print(-1)












