import sys

input=sys.stdin.readline

T=int(input())





for _ in range(T):
    
    N,M=map(int,input().split())
    D=[[0 for _ in range(N+1)]for _ in range(M+1)]

    D[1][1]=1

    #
    for i in range(1,M+1):
        D[i][1]=i


    for j in range(2,N+1):
        D[j][j]=1
        for i in range(j+1,M+1):
            D[i][j]=D[i-1][j]+D[i-1][j-1]

        
        # for i in D:
        #     print(i)
    
    print(D[M][N])


    
'''
    0   1   2   3   4   5   ... M
0   0   0   0   0   0   0      
1   0   1   2   3   4   5
2   0   0   1   3   6   10
3
.
N




1
3 6

'''



