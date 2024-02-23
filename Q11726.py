import sys
sys.setrecursionlimit(100000)


input=sys.stdin.readline

n=int(input())


memo={}

def DP(n):
    if n<0:
        return 0
    elif n==0:
        return 1

    if n in memo:
        return memo[n]


    memo[n]=DP(n-1)+DP(n-2)
    return memo[n]


print(DP(n)%10007)



