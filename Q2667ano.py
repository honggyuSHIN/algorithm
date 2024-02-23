from collections import deque
N = int(input())
array = []
for _ in range(N):
    array.append([int(i) for i in input().replace("\n", "")])

danjis = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if array[i][j] == 0:
            continue
        array[i][j] = 0
        count = 1
        deq = deque([[i, j]])
        while(len(deq) != 0):
            
            for _ in range(len(deq)):
                x, y = deq.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and nx < N and ny >= 0 and ny < N and array[nx][ny]:
                        array[nx][ny] = 0
                        deq.append([nx, ny])
                        count += 1
        danjis.append(count)
danjis.sort()
print(len(danjis))
for d in danjis:
    print(d)