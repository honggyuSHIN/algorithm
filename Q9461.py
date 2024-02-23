import sys
input=sys.stdin.readline

'''
1, 1, 1, 2, 2, 3, 4, 5, 7, 9

'''
start=8
cnt=4

D=[0,1,1,1,2,2,3,4,5,7,9]
T=int(input())

def DP(n):
    for i in range(11,n+1):
        D.append(D[i-2]+D[i-3])


li=[]
for _ in range(T):
    li.append(int(input()))

for i in li:
    try:
        print(D[i])
    except:
        DP(i)
        print(D[i])






