from queue import PriorityQueue
import sys

input=sys.stdin.readline


V,E=map(int,input().split())
start=int(input())

visited=[False]*(V+1)
distance=[sys.maxsize]*(V+1)
q=PriorityQueue()
q.put((0,start))
li=[[] for i in range(V+1)]

distance[start]=0

# 담기
for i in range(E):
    u,v,w=map(int,input().split())
    # u에서 v로, 가중치 w
    li[u].append((v,w))

# 큐 꺼내기
while q.qsize()>0:
    queue=q.get()
    weight=queue[0]
    node=queue[1]
    # node : 현재 위치.

    if visited[node]==True:
        # 큐에서 방문했던 노드가 나오면 끝.
        continue

    visited[node]=True
    # distance는 방문 전에 연결됐던 노드에서 갱신됐을 것임.

    
    for i in li[node]:
        # 방문 안했던 노드가 나오면 그 노드에서 연결된 곳들의 거리를 갱신해주고
        # 우선순위 큐에 넣어서 다음에 어디 갈 지 정함.
        next=i[0]
        size=i[1]
        
        if distance[next]>distance[node]+size:
            distance[next]=distance[node]+size
        q.put((size,next))
for i in range(1,len(distance)):
    if visited[i]==True:
        print(distance[i])
    else:
        print("INF")



'''
큐에는 처음에 (0,시작) 넣어줘서 시작으로 향하게 함.
시작으로 가서 ex)3번 노드.
3번 노드가 다음에 어디로 가는지 다 li에서 꺼내서 갱신해줌.
갱신하면서 visited도 갱신해주나? 왜지?
갱신하면서 다 큐에 넣어주면 되나? 흠.



'''

'''
<다익스트라>
한번 방문한 노드는 다시 방문하지 않음. -> visited를 통해 관리
새로운 노드 후보가 있을 때 후보가 갈 수 있는 노드들까지의 거리는 갱신함. 
하지만 아직 방문한 것은 아니고 그 거리들 중에서 제일 작은 쪽으로 방문함.
방문할 수 있는 노드 전체 중에서 제일 작은 쪽으로 가는 것임. 최근에 방문한 노드
쪽으로만 가야할 필요 없음.
1 -> 3 으로 진행되고 있다고 3에 근접한 노드들 중에서만 최소값을 확인하는 게 아니라
1과 근접한 노드들도 후보 대상임.
-> 우선순위큐의 기준을 가중치로 두는 이유.



'''







