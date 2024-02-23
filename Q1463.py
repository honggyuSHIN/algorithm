from collections import deque
import sys
input=sys.stdin.readline

N=int(input())

q=deque()
visited=[0]*(N+1)
q.append((N,0))

while q:
    n,cnt=q.popleft()
    if n==1:
        print(cnt)
        break
    cnt+=1
    if n%3==0:
        if visited[n//3]==0:
            visited[n//3]=1
            q.append((n//3,cnt))
    if n%2==0:
        if visited[n//2]==0:
            visited[n//2]=1
            q.append((n//2,cnt))
    if visited[n-1]==0:
        visited[n-1]=1
        q.append((n-1,cnt))