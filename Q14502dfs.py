import sys
import copy
from itertools import combinations
input=sys.stdin.readline

N,M=map(int,input().split())
# 세로 N    가로 M

lab=[]

for _ in range(N):
    lab.append(list(map(int,input().split())))


zero=[]
two=[]
onecnt=0

for i in range(N):
    for j in range(M):
        if lab[i][j]==0:
            zero.append((i,j))
        if lab[i][j]==2:
            two.append((i,j))
        if lab[i][j]==1:
            onecnt+=1


dn=[1,-1,0,0]
dm=[0,0,1,-1]

def spread(i,j):
    global total

    for k in range(4):
        nn=i+dn[k]
        nm=j+dm[k]
        if 0<=nn<N and 0<=nm<M:
            if testlab[nn][nm]==0:
                testlab[nn][nm]=2
                total-=1
                spread(nn,nm)

            
maxcnt=0


for walls in combinations(zero,3):
    total=len(zero)-3
    testlab=copy.deepcopy(lab)

    for i,j in walls:
        testlab[i][j]=1

    

    for i,j in two:
        spread(i,j)
    
    if total>maxcnt:
        maxcnt=total
    # print(f"total : {total}")
    # print(f"maxcnt : {maxcnt}")

    # for i in testlab:
    #     print(i)

    # print()


print(maxcnt)












