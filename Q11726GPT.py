import sys

sys.setrecursionlimit(100000)

input_value = int(input())

memo = {}  # 메모이제이션을 위한 딕셔너리

def DP(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1

    # 이미 계산된 값이 있다면 그 값을 반환
    if n in memo:
        return memo[n]

    # 재귀적으로 호출하여 계산하고 메모에 저장
    memo[n] = DP(n-1) + DP(n-2)
    return memo[n]

result = DP(input_value) % 10007
print(memo)
print(result)
