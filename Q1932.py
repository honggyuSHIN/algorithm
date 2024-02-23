import sys

input=sys.stdin.readline

N=int(input())

tri=[]

for _ in range(N):
    tri.append(list(map(int,input().split())))

D=[]
for i in range(N):
    D.append([0]*(i+1))

def DP(n,k):

    if n<0:
        return
    
    if D[n][k]!=0:
        return D[n][k]
    
    if n==0:
        return tri[0][0]

    

    if n==len[tri[n-1]]:
        return DP(n-1,k)
    
    D[n][k]=max(DP(n-1,k),DP(n-1,k+1))
    return 


for i in range(N):
    DP(N-1,i)










