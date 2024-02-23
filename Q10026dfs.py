from collections import deque
import sys
sys.setrecursionlimit(10000)
N=int(input())

table=[[] for _ in range(N)]
table02=[[] for _ in range(N)]

dn=[1,-1,0,0]
dm=[0,0,1,-1]


for i in range(N):
    table[i]=list(input())
    table02[i].extend(table[i])


def dfsgood(n,m,color):
    table[n][m]=0

    for i in range(4):
        nn=n+dn[i]
        nm=m+dm[i]

        if 0<=nn<N and 0<=nm<N and table[nn][nm]==color:
            dfsgood(nn,nm,color)



cnt=0



for i in range(N):
    for j in range(N):
        if table[i][j]!=0:
            dfsgood(i,j,table[i][j])
            cnt+=1


print(cnt,end=' ')





cnt=0

dn=[1,-1,0,0]
dm=[0,0,1,-1]

q=deque()

def dfsbad(n,m,color):
    

    q.append((n,m,color))

    while q:
        n,m,color=q.popleft()
        if color=='G':
            secondcolor='R'
        elif color=='R':
            secondcolor='G'
        elif color=="B":
            secondcolor="B"

        
        for i in range(4):
            nn=n+dn[i]
            nm=m+dm[i]
            if 0<=nn<N and 0<=nm<N :
                if table02[nn][nm]==color or table02[nn][nm]==secondcolor:
                    table02[nn][nm]=0
                    q.append((nn,nm,color)) 

    



for i in range(N):
    for j in range(N):
        if table02[i][j]!=0:
            dfsbad(i,j,table02[i][j])
            table02[i][j]=0
            cnt+=1



print(cnt)

