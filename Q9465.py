import sys

input=sys.stdin.readline

T=int(input())



for _ in range(T):
    n=int(input())
    li=[]
    li.append([0 for _ in range(n)])
    D=[]
    D.append([0 for _ in range(n)])
    for _ in range(2):
        li.append(list(map(int,input().split())))
        D.append([0]*n)

    D[1][0]=li[1][0]
    D[2][0]=li[2][0]
    for j in range(1,n):
        for i in range(3):
            # i : 리스트 선택   j : 항목 선택
            if i==0:
                D[i][j]=max(D[1][j-1],D[2][j-1])
            elif i==1:
                D[i][j]=max(D[2][j-1],D[0][j-1])+li[i][j]
            elif i==2:
                D[i][j]=max(D[1][j-1],D[0][j-1])+li[i][j]




    print(max(D[0][n-1],D[1][n-1],D[2][n-1]))



    # print()
    # print()

    # for i in li:
    #     print(i)
    # print()
    # for i in D:
    #     print(i)
    # print()
    # print()


    '''
1
1
50
40
    
    



2
4
50 40 19 18
40 20 40 20
4
40 40 39 40
40 40 40 40
    '''