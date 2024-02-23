import sys
input=sys.stdin.readline
N=int(input())
D=[[0 for _ in range(2)]for _ in range(N+1)]

D[1][0]=0
D[1][1]=1

# D[2][0]=1
# D[2][1]=0

if N>=2:
    for i in range(2,N+1):
        D[i][0]=D[i-1][0]+D[i-1][1]
        D[i][1]=D[i-1][0]

print(D[N][0]+D[N][1])
