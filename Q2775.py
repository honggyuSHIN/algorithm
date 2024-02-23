import sys

input=sys.stdin.readline

T=int(input())


apart=[[i for i in range(15)]for _ in range(15)]




for k in range(1,15):
    for n in range(1,15):
        if n==1:
            continue
        apart[k][n]=apart[k][n-1]+apart[k-1][n]


for _ in range(T):
    k=int(input())
    n=int(input())
    print(apart[k][n])
