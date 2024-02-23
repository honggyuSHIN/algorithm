from collections import deque
import copy
from itertools import combinations

N,M=map(int,input().split())
# N : 세로  M : 가로

lab=[]

for _ in range(N):
    lab.append(list(map(int,input().split())))

two=[]
zero=[]

for i in range(N):
    for j in range(M):
        if lab[i][j]==2:
            two.append((i,j))
        if lab[i][j]==0:
            zero.append((i,j))

dn=[1,-1,0,0]
dm=[0,0,1,-1]

q=deque()

def spread(a,b):
    q.append((a,b))
    while q:
        n,m=q.popleft()

        for i in range(4):
            nn=n+dn[i]
            nm=m+dm[i]
            if 0<=nn<N and 0<=nm<M:
                if testlab[nn][nm]==0:
                    testlab[nn][nm]=2
                    q.append((nn,nm))

maxcnt=0

for walls in combinations(zero,3):
    testlab=copy.deepcopy(lab)

    # 벽 세우기
    for n,m in walls:
        testlab[n][m]=1

    for n,m in two:
        spread(n,m)
    
    cnt=0
    for i in range(N):
        for j in range(M):
            if testlab[i][j]==0:
                cnt+=1
    
    if maxcnt<cnt:
        maxcnt=cnt

print(maxcnt)
















