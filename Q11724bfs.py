import sys
from collections import deque


# 시간 초과 발생.
input=sys.stdin.readline
sys.setrecursionlimit(10000)

N,M=map(int,input().split())

q=deque()


visited=[False]*(N+1)
table=[[]for _ in range(N+1)]

for _ in range(M):
    start,end=map(int,input().split())
    table[start].append(end)
    table[end].append(start)


def bfs(start):
    global li
    q.append(start)
    visited[start]=True
    while q:
        current=q.popleft()
        
        for i in table[current]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
        

cnt=0
for i in range(1,N+1):
    if visited[i]==False:
        bfs(i)
        cnt+=1

        



print(cnt)

