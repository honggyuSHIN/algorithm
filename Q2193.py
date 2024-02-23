import sys
input=sys.stdin.readline

N=int(input())

D0=[0]*(N+2)
D1=[0]*(N+2)
D0[0]=0
D1[0]=0

D1[1]=1

D0[2]=1



if N>=3:
    for i in range(2,N+1):
        # 1로 끝나는 애가 있을 때.
        if D1[i-1]!=0:
            D0[i]=D0[i-1]+D1[i-1]
        else:
            D0[i]=D0[i-1]
        D1[i]=D0[i-1]


if D1[N]!=0:
    print(D1[N]+D0[N])
else:
    print(D0[N])
