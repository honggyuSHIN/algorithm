import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

tree=[[]for _ in range(N+1)]
# 0은 제외, 1부터 N까지

for _ in range(N-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

answer=[0]*(N+1)

q=deque()
q.append(1)

while q:
    temp=q.popleft()
    for i in tree[temp]:
        if answer[i]==0:
            answer[i]=temp
            q.append(i)

for i in range(2,N+1):
    print(answer[i])












