def dfs(maze, x, y, count, visited):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        return count + 1  # 도착 지점에 도달했을 때 이동한 칸 수 반환

    visited.add((x, y))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1 and (nx, ny) not in visited:
            result = dfs(maze, nx, ny, count + 1, visited)
            if result > 0:
                return result

    return 0  # 도착 지점에 도달할 수 없는 경우

# 입력 받기
N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

# DFS 호출
result = dfs(maze, 0, 0, 1, set())

# 결과 출력
print(result)
