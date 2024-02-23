import sys
from collections import deque
input=sys.stdin.readline

N,M,V=map(int,input().split())

arr=[[]for _ in range(N+1)]


for i in range(M):
    v1,v2=map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

# 정렬 및 중복 제거
for i in range(len(arr)):
    arr[i].sort()
    newset=set(arr[i])
    arr[i]=list(newset)


visited=[False]*(N+1)
# visited[V]=True

mydeque=deque()
# mydeque.append(V)



def bfs(a):
    global visited
    global mydeque
    global arr

    if visited[a]==False:
        print(a,end=' ')
        visited[a]=True
        for i in arr[a]:
            mydeque.append(i)
    elif visited[a]==True:
        pass
    if len(mydeque)>0:
        bfs(mydeque.popleft())

bfs(V)

print()

visited=[False]*(N+1)
# visited[V]=True

mydeque=deque()
# mydeque.append(V)
print(arr)
print(visited)

def dfs(a):
    global visited
    global mydeque
    global arr
    print(a)
    print(visited)
    if visited[a]==False:
        print(a, end=' ')
        visited[a]==True
        for i in arr[a]:
            dfs(i)

    
dfs(V)













# print(V,end=' ')

# while mydeque:
#     if visited.count(True)==N:
#         break
#     temp=mydeque.popleft()
#     for i in arr[temp]:
#         if visited[i]==False:
#             visited[i]=True
#             print(i,end=' ')
#             for i in arr[temp]:
#                 mydeque.append(i)

    


















