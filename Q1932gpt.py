import sys

input = sys.stdin.readline

N = int(input())

tri = []

for _ in range(N):
    tri.append(list(map(int, input().split())))

# DP 테이블 초기화
D = [[0] * N for _ in range(N)]
D[0][0] = tri[0][0]

# Bottom-up 방식으로 DP 테이블 채우기
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:  # 맨 왼쪽 끝 열일 경우
            D[i][j] = D[i - 1][j] + tri[i][j]
        elif j == i:  # 맨 오른쪽 끝 열일 경우
            D[i][j] = D[i - 1][j - 1] + tri[i][j]
        else:  # 중간에 있는 열일 경우
            D[i][j] = max(D[i - 1][j - 1], D[i - 1][j]) + tri[i][j]

# 마지막 행에서 최댓값 찾기
max_sum = max(D[N - 1])

print(max_sum)
