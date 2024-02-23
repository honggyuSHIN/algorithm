import sys
from queue import PriorityQueue
input=sys.stdin.readline

V,E=map(int,input().split())


uf=[]
for i in range(V+1):
    uf.append(i)

q=PriorityQueue()
# 작은 숫자 기준.

for i in range(E):
    s,e,w=map(int,input().split())
    q.put((w,s,e))


def find(v):
    if v==uf[v]:
        return v
    else:
        uf[v]=find(uf[v])
        return uf[v]



def union(a,b):
    global cnt
    global allcnt
    if find(a)==find(b):
        pass
    elif find(a)>find(b):
        uf[a]=uf[b]
    elif find(a)<find(b):
        uf[b]=uf[a]

        
cnt=0
allcnt=0

# q : (가중치,시작,끝)
while cnt<(V-1):
    w,s,e = q.get()
        
    if find(s)!=find(e):
        union(s,e)
        cnt+=1
        allcnt+=w


print(allcnt)
    

'''
3 3
1 3 3
2 3 2
1 2 1

'''







