import sys

input=sys.stdin.readline


n=int(input())
D=[[1 for _ in range(10)]for _ in range(n)]
D[0][0]=0
for i in range(1,n):
    for j in range(10):
        if j==0:
            D[i][j]=D[i-1][1]
        elif j==9:
            D[i][j]=D[i-1][8]    

        else:    
            D[i][j]=D[i-1][j-1]+D[i-1][j+1]



print(sum(D[n-1])%1000000000)
