import sys

input=sys.stdin.readline

N=int(input())

tri=[]
for _ in range(N):
    tri.append(list(map(int,input().split())))

ans=[]
for i in range(N):
    ans.append([0]*(i+1))


def DP(n,k):

    if n<0 or k<0:
        return 0
    if n==0:
        ans[0][0]=tri[0][0]
        return ans[0][0]

    if ans[n][k]!=0:
        return ans[n][k]
    

    if k==0:
        ans[n][k]=DP(n-1,k)+tri[n][k]
    else:
        try:
            ans[n][k]=max(DP(n-1,k)+tri[n][k],DP(n-1,k-1)+tri[n][k])
        except:
            ans[n][k]=DP(n-1,k-1)+tri[n][k]

    return ans[n][k]


for i in range(N):
    DP(N-1,i)

print(max(ans[N-1]))





