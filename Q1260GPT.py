from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

table = [[] for _ in range(N + 1)]

# 입력받기.
for _ in range(M):
    num01, num02 = map(int, input().split())
    table[num01].append(num02)
    table[num02].append(num01)

# 정렬하기
for i in range(1, N + 1):
    table[i].sort()

visited = [False] * (N + 1)


def dfs(num01):
    if visited[num01] == True:
        return

    visited[num01] = True
    print(num01, end=' ')
    for i in table[num01]:
        dfs(i)


dfs(V)
print()

q = deque()
cnt = 0

visited = [False] * (N + 1)


def bfs(start):
    global visited
    q = deque([start])
    visited[start] = True

    while q:
        current = q.popleft()
        print(current, end=' ')
        
        for neighbor in table[current]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True


bfs(V)
