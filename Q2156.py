

n=int(input())

grapes=[]
for _ in range(n):
    grapes.append(int(input()))

D=[[0,0,0]for _ in range(n)]
D[0][0]=0
D[0][1]=grapes[0]

for i in range(1,n):
    D[i][0]=max(D[i-1][0],D[i-1][1],D[i-1][2])
    D[i][1]=D[i-1][0]+grapes[i]
    D[i][2]=D[i-1][1]+grapes[i]

print(max(D[n-1]))