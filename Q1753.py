# 다익스트라.

import sys
input=sys.stdin.readline
from queue import PriorityQueue

V,E=map(int,input().split())
K=int(input())
distance=[sys.maxsize]*(V+1)
# 0번 인덱스 안 쓰려고 V+1함.
visited=[False]*(V+1)
myList=[[] for _ in range(V+1)]
q=PriorityQueue()


for _ in range(E):
    # 1 2 8 : 1에서 2, 가중치 8을 0번 인덱스는 비우고 1번 인덱스에 (2,8) 튜플 형태로 
    #           넣어줌.
    u,v,w=map(int,input().split())
    myList[u].append((v,w))


q.put((0,K))
# 0번째 인덱스에 가중치 0을 넣고 1번째 인덱스에 K노드를 넣음.

distance[K]=0

while q.qsize()>0:
    current=q.get()
    print(f"current : {current}")
    c_v=current[1]  # 위의 (0,K)에서 K에 접근하기 위함.
    if visited[c_v]:
        continue
    visited[c_v]=True

    for tmp in myList[c_v]:
        # 2 -> (4,5) (5,2)로 이어질 때 4,5는 노드 5,2는 가중치.
        # 이게 myList의 c_v인덱스 안에 저장되는 것 같음.
        next=tmp[0]     # 다음 노드
        value=tmp[1]    # 가중치

        if distance[next]>distance[c_v]+value:
            # 새로 추가된 길이 더 작을 경우.
            # 노드에 닿았을 때 거리 비교하는 거 구현한 거임.
            distance[next]=distance[c_v]+value
            q.put((distance[next],next))

            # 업데이트 됐을 때만 큐를 갱신?



for i in range(1,V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")










# 유튜브에서 우선순위 큐 강의 보기.
'''
스택(Stack) : 가장 나중에 삽입된 데이터가 추출됨.
큐(Queue) : 가장 먼저 삽입된 데이터가 추출됨.
우선순위 큐(Priority Queue) : 가장 우선순위가 높은 데이터가 추출됨.


'''

