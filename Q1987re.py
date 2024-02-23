import sys
import copy
input=sys.stdin.readline

table=[]

dn=[1,-1,0,0]
dm=[0,0,1,-1]








R,C=map(int,input().split())
# R : 세로  C : 가로

D=[[0 for _ in range(C)]for _ in range(R)]


def bfs(r,c,arr):
    # r : 세로 c : 가로
    



    for i in range(4):
        ar=copy.deepcopy(arr)
        nr=r+dn[i]
        nc=c+dm[i]
        if 0<=nr<R and 0<=nc<C:
            try:
                if arr not in D[nr][nc]:
                    D[nr][nc]
                    ar.add(table[nr][nc])
                    bfs(nr,nc,ar)
            except:
                D[nr][nc]
                ar.add(table[nr][nc])
                bfs(nr,nc,ar)

for _ in range(R):
    table.append(list(input().strip()))


arr=set()
arr.add(table[0][0])
D[0][0]=arr

bfs(0,0,arr)

cnt=0
for i in D:
    for j in i:
        if cnt<len(j):
            cnt=j

print(cnt)







