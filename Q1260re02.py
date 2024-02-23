from collections import deque
import sys
input=sys.stdin.readline

N,M,V=map(int,input().split())


table=[[] for _ in range(N+1)]
visited=[False]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    table[a].append(b)
    table[b].append(a)


for i in range(N+1):
    table[i].sort()


def dfs(node):
    if visited[node]==True:
        return
    visited[node]=True
    print(node, end=' ')

    for i in table[node]:
        if visited[i]==False:
            dfs(i)


dfs(V)
print()


q=deque()
visited=[False]*(N+1)


def bfs(start):
    q.append(start)
    if visited[start]==True:
        return


    while q:
        current=q.popleft()
        if visited[current]==False:
            visited[current]=True

            print(current,end=' ')
            for i in table[current]:
                if visited[i]==False:
                    q.append(i)
        


bfs(V)












