from collections import deque 

N,M=map(int,input().split())


q=deque()

visited=[0]*100001


q.append(N)

while q:
    current=q.popleft()
    if current==M:
        print(visited[current])
        break

    for i in (current+1,current*2,current-1):
        if 0<=i<=100000:
            if visited[i]==0 or visited[i]>visited[current]:
                visited[i]=visited[current]+1

                q.append(i)












'''
이해 안되는 거


#### 정답 ####
from collections import deque
n, k = map(int,input().split())
graph=[0]*1000001
def bfs(n,k):
    q = deque()
    q.append(n)
    graph[n] = 1
    while q:
        n = q.popleft()
        if n == k:
            print(graph[n]-1)
            return
        for nn in (n+1,n-1,n*2):
            if 0<=nn<=100000:
            

            ####
                if not graph[nn] or graph[nn] > graph[n]+1:
                    graph[nn] = graph[n] + 1
                    q.append(nn)
bfs(n,k)





'''



