import sys

input=sys.stdin.readline

N=int(input())

D=[0]*31

D[2]=3
D[4]=D[2]*D[2]+2

for i in range(6,31,2):
    temp=i-4
    D[i]=D[i-2]*D[2]*2+2*((i-4)//2)


'''
D[2]=3
D[4]=D[2]*2+2
D[6]=       2/4             6
            D[4]*2*D[2]     +2   
D[8]=D[6]*2*D[2]        +2


'''

print(D[N])
