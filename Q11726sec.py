import sys
sys.setrecursionlimit(100000)


input=sys.stdin.readline

n=int(input())





D=[0]*(n+3)
D[1]=1
D[2]=2

if n>=3:
    for i in range(3,n+1):
        D[i]=D[i-1]+D[i-2]

print(D[n]%10007)



