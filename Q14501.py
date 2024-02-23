import sys

input=sys.stdin.readline

N=int(input())
t=[]
p=[]

for _ in range(N):
    T,P=(map(int,input().split()))
    t.append(T)
    p.append(P)

D=[0 for _ in range(N+1)]
# D[i] : i일차에 얻을 수 있는 최대 가치

D[0]=0

for i in range(N+1):
    try:
        if D[i]==0:
            if i!=0:
                D[i]=max(D[:i])
        D[i+t[i]]=max(D[i]+p[i],D[i+t[i]])
        
    except:
        pass



print(max(D))


'''
    1   2   3   4   5
0   
1




'''


