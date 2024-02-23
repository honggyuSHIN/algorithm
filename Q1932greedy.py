import sys

'''
DP는 이전 항목들이 채워져있다고 가정하고 코드를 생각해야 함.

아래 코드의 경우 나아가며 진행하기 때문에 보기에만 DP일 뿐 너비우선탐색과 다르지 않음.
코드 자체를 이전 항에서 가져와서 계산하면 항목당 한번의 계산만 하지만
아래 코드는 항목당 2번씩 계산해야 함.

'''

input=sys.stdin.readline

N=int(input())

D=[]
for i in range(N):
    D.append([0]*(i+1))



def DP(n,k):
    # n행의 k
    if n>=N:
        return
    
    if n+1<N:
        if D[n+1][k]<D[n][k]+tri[n+1][k]:
            D[n+1][k]=D[n][k]+tri[n+1][k]
            DP(n+1,k)

        if D[n+1][k+1]<D[n][k]+tri[n+1][k+1]:
            D[n+1][k+1]=D[n][k]+tri[n+1][k+1]
            DP(n+1,k+1)
    


tri=[]

for _ in range(N):
    tri.append(list(map(int,input().split())))

D[0]=tri[0]
DP(0,0)

print(max(D[N-1]))
