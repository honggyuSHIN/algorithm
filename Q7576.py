import sys
from collections import deque
imput=sys.stdin.readline



M,N=map(int,input().split())
# M : 가로
# N : 세로

tomato=[[]for _ in range(N)]

for i in range(N):
    tomato[i].extend(list(map(int,input().split())))


q=deque()


# i 세로 j 가로     인덱스
# 시작 포인트 수집. 1 수집하기
for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            q.append((i,j,0))




# def bfs(n,m):
#     # n : 세로 m : 가로  인덱스
#     if tomato[n][m]==0 or tomato[n][m]==-1:
#         return
#     q.append((n,m))

#     while q:

#     pass

# for n,m in start:
#     q.append((n,m,0))


dn=[1,-1,0,0]
dm=[0,0,1,-1]

# 최대값
ccnt=0

# start만 먼저 하기
for _ in range(len(q)):
    n,m,c=q.popleft()
    tomato[n][m]=1
    c+=1

    if ccnt<c:
        ccnt=c
    
    for i in range(4):
        nn=n+dn[i]
        nm=m+dm[i]

        if 0<=nn<N and 0<=nm<M and tomato[nn][nm]==0:
            q.append((nn,nm,c))


# start에서 추가한 것을 토대로 마저 하기.
while q:

    n,m,c=q.popleft()
    if tomato[n][m]==0:     ###
        tomato[n][m]=1
        c+=1

        if ccnt<c:
            ccnt=c
        
        for i in range(4):
            nn=n+dn[i]
            nm=m+dm[i]

            if 0<=nn<N and 0<=nm<M and tomato[nn][nm]==0:
                q.append((nn,nm,c))


flag=False

for i in range(N):
    for j in range(M):
        if tomato[i][j]==0:
            flag=True




if flag:
    print(-1)
    
else:
    print(ccnt-1)


# if flag:
#     print(-1)
# else:
#     print(ccnt-1)






