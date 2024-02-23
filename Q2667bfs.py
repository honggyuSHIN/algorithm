from collections import deque
import sys

# 틀림. 예제는 맞는데

input=sys.stdin.readline


N=int(input())

table=[[]for _ in range(N)]


for i in range(N):
    table[i].extend(map(int,input().strip()))


# 0~N-1
    
q=deque()

cnt=0
cntsave=[]
allcnt=0

dy=[-1,1,0,0]
dx=[0,0,-1,1]


def bfs(a,b):
    global cnt
    global allcnt
    # if table[y][x]==0:
    #     return
    q.append((a,b))
    
    while q:
        y,x=q.popleft()

        if table[y][x]==1:  

            table[y][x]=0
            cnt+=1

            for i in range(len(dy)):
                ny=y+dy[i]
                nx=x+dx[i]
                if 0<=ny<N and 0<=nx<N and table[ny][nx]==1:
                    q.append((ny,nx))


    # allcnt+=1
    cntsave.append(cnt)



for i in range(N):
    for j in range(N):
        if table[i][j]==1:
            
            bfs(i,j)
            cnt=0
            allcnt+=1

cntsave.sort()


# cntsave.sort()

print(allcnt)
for i in cntsave:
    print(i)












'''

5
00100
00000
00000
00000
00000


'''




