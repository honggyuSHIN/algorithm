# 벨만 포드
import sys

input=sys.stdin.readline


N,M=map(int,input().split())
visited=[False]*(N+1)
distance=[sys.maxsize]*(N+1)
li=[]

distance[1]=0
visited[1]=True


for i in range(M):
    s,e,w=map(int,input().split())
    li.append((s,e,w))

for _ in range(N-1):
    visit=[]
    for start,end,time in li:
        # 방문한 곳에서 시작함.
      
        if visited[start]==True:
            if distance[end]>distance[start]+time:
                distance[end]=distance[start]+time
                visit.append(end)
    for i in visit:
        visited[i]=True

# 한번 더 실행해서 바뀌면 루프 있는 거임.
dis_save=[]
cycle=False
for i in distance:
    dis_save.append(i)


for start,end,time in li:    
    if visited[start]==True:
        if distance[end]>distance[start]+time:
            cycle=True


if cycle==True:
    print(-1)
else:
    for i in range(2,N+1):
        if visited[i]==True:
            print(distance[i])
        else:
            print(-1)










