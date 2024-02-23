import sys
from itertools import combinations
input=sys.stdin.readline

# D를 정의해야 함.

n,k=map(int,input().split())

coins=[]

for i in range(n):
    coin=int(input())
    coins.append(coin)


cnt=0
def DP(n):
    global cnt
    if n==0:
        cnt+=1
    for i in coins:
        if n-i>=0:
            DP(n-i)

up=max(coins)



'''
1 2 5

    0   1   2   3   4   5   6   7   8   9   10
1       1   1   1   1   1   1   1   1   1   1    
2       1   2   2   3   3   4   4   5   5   6
5       1   2   2   3   4   5   6   7   8   9        


'''







