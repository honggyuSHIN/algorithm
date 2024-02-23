import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)


N,M=map(int,input().split())

table=[[]for _ in range(N+1)]
visited=[False]*(N+1)



for _ in range(M):
    start,end=map(int,input().split())
    table[start].append(end)    
    table[end].append(start)


cnt=0

def dfs(start):
    if visited[start]==True:
        return

    visited[start]=True

    for i in table[start]:
        if visited[i]==False:
            dfs(i)



for i in range(1,N+1):
    if visited[i]==False:
        dfs(i)
        cnt+=1


print(cnt)



















