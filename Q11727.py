import sys

input=sys.stdin.readline

n=int(input())

D=[0]*(n+1)

D[1]=1
if n>=2:
    D[2]=3

if n>=3:
    for i in range(3,n+1):
        D[i]=D[i-2]*2+D[i-1]

print(D[n]%10007)




