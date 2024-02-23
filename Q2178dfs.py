'''
최단거리 문제는 bfs로 푸는 게 좋음.
dfs에서 인수 넘겨서 카운트해도 table에 갱신하는 방법 밖에는 없어보임.


'''




import sys

N,M=map(int,input().split())
# N 세로        0~(N-1)
# M 가로        0~(M-1)

table=[[]for _ in range(N)]

for i in range(N):
    table[i]=list(map(int,input()))

# visited=[[False for _ in range(M)]for _ in range(N)]

dn=[1,-1,0,0]
dm=[0,0,1,-1]

for i in range(N):
    for j in range(M):
        if table[i][j]==1:
            table[i][j]=1000000




save=[]
def dfs(n,m,cnt):

    if table[n][m]==0:
        return
    cnt+=1

    if n==N-1 and m==M-1:
        save.append(cnt)

    if table[n][m]<cnt:
        return

    if table[n][m]>cnt:
        table[n][m]=cnt
    
    for i in range(4):
        nn=n+dn[i]
        nm=m+dm[i]
        if 0<=nn<N and 0<=nm<M and table[nn][nm]!=0:
            dfs(nn,nm,cnt)
            
        # for i in table:
        #         print(i)
    
    return cnt



cnt=dfs(0,0,0)



# for i in range(N):
#     for j in range(M):
#         dfs(i,j)



answer=min(save)
print(answer)
















