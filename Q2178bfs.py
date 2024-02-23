import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

table=[[]for _ in range(N+1)]

table[0]=[0]*(M+1)

for i in range(1,N+1):
    table[i].append(0)
    table[i].extend(list(map(int,input().strip())))


q=deque()


q.append((1,1,0))

cnt=0

dn=[1,-1,0,0]
dm=[0,0,1,-1]


while q:
    n,m,cnt=q.popleft()


    if n==N and m==M:
        cnt+=1
        print(cnt)
        break

    elif table[n][m]==1:
        table[n][m]=0
        cnt+=1


        for i in range(4):
            nn=n+dn[i]
            nm=m+dm[i]
            if 0<nn<=N and 0<nm<=M and table[nn][nm]==1:
                q.append((nn,nm,cnt))
            
















