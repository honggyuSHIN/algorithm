import sys
from collections import deque
input=sys.stdin.readline

N=int(input())

D=[sys.maxsize]*(N+1)

start1=3

start2=5
D[start1]=1
if N>=5:
    D[start2]=1

q=deque()
q.append((3,1))
q.append((5,1))



while q:
    current,cnt=q.popleft()

    if current+5<=N:
        if D[current+5]>cnt+1:
            D[current+5]=cnt+1
            q.append((current+5,cnt+1))
            
        if D[current+3]>cnt+1:
            D[current+3]=cnt+1
            q.append((current+3,cnt+1))
    
    elif current+3<=N:

            
        if D[current+3]>cnt+1:
            D[current+3]=cnt+1
            q.append((current+3,cnt+1))


if D[N]==sys.maxsize:
    print(-1)
else:
    print(D[N])

for i in range(N):
    if D[i]==sys.maxsize:
        D[i]=0
print(D)