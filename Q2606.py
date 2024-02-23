import sys
from collections import deque
# 깊이 너비 둘 다 풀어보기

# 컴퓨터 수
V=int(input())
# 엣지 수
E=int(input())

table=[[]for _ in range(V+1)]


for i in range(E):
    num01,num02=map(int,input().split())
    table[num01].append(num02)
    table[num02].append(num01)



visited=[False]*(V+1)
cnt=0

def dfs(node):
    global cnt
    if visited[node]==True:
        return
    visited[node]=True
    cnt+=1

    for i in table[node]:
        if visited[i]==False:
            dfs(i)



# dfs(1)
# print(cnt-1)
            
q=deque()


cnt=0
visited=[False]*(V+1)


def dfs(node):
    global cnt
    if visited[node]==True:
        return
    
    q.append(node)
    
    while q:
        current=q.popleft()

        if visited[current]==False:
            visited[current]=True
            cnt+=1
            for i in table[current]:
                if visited[i]==False:
                    q.append(i)

dfs(1)
print(cnt-1)








