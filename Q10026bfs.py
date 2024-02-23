from collections import deque

N=int(input())

table=[[]for _ in range(N)]
table02=[[]for _ in range(N)]

for i in range(N):
    table[i]=list(input())
    table02[i].extend(table[i])
dn=[1,-1,0,0]
dm=[0,0,1,-1]

q=deque()
cnt=0
def bfsgood(n,m,color):
    q.append((n,m,color))
    table[n][m]=0
    while q:
        n,m,color=q.popleft()
        for i in range(4):
            nn=n+dn[i]
            nm=m+dm[i]
            if 0<=nn<N and 0<=nm<N and table[nn][nm]==color:
                table[nn][nm]=0
                q.append((nn,nm,color))



for i in range(N):
    for j in range(N):
        if table[i][j]!=0:
            
            bfsgood(i,j,table[i][j])

            cnt+=1

print(cnt,end=' ')


###


q=deque()
cnt=0

def bfsbad(n,m,color):
    table02[n][m]=0
    q.append((n,m,color))

    while q:
        n,m,color=q.popleft()
        if color=="R":
            secondcolor="G"
        elif color=="G":
            secondcolor="R"
        elif color=="B":
            secondcolor="B"


        for i in range(4):
            nn=n+dn[i]
            nm=m+dm[i]

            if 0<=nn<N and 0<=nm<N:
                if table02[nn][nm]==color or table02[nn][nm]==secondcolor:
                    table02[nn][nm]=0
                    q.append((nn,nm,color))
                






for i in range(N):
    for j in range(N):
        if table02[i][j]!=0:
            
            bfsbad(i,j,table02[i][j])

            cnt+=1




print(cnt)




