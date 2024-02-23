import sys

input=sys.stdin.readline

N=int(input())


P=list(map(int,input().split()))
P.insert(0,0)
D=[0 for _ in range(N+1)]

D[1]=P[1]

for i in range(2,N+1):
    for j in range(1,i+1):
        if D[i]<D[i-j]+P[j]:
            D[i]=D[i-j]+P[j]


print(D[N])


'''

10

0   5   2           8           10
0   5   100         8           10
        5+5         100+5         
                    5+5+5

        100         105
'''
