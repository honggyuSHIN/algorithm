import sys

input=sys.stdin.readline


N=int(input())

D=[[0 for _ in range(10)]for _ in range(N)]


for i in range(N):
    for j in range(10):
        if i==0:
            D[i][j]=1
        else:
            for k in range(j+1):
                D[i][j]+=D[i-1][k]


print(sum(D[N-1])%10007)


