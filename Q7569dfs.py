# dfs로는 안 되는데... bfs로 다시 풀 것.

M,N,H=map(int,input().split())

# M : 가로   N : 세로   H : 높이


tomatoes=[[[]for _ in range(N)]for _ in range(H)]
# 높이 - 세로 - 가로 순서로 접근.


for i in range(H):
    for j in range(N):
        tomatoes[i][j]=list(map(int,input().split()))


dm=[1,-1,0,0,0,0]
dn=[0,0,1,-1,0,0]
dh=[0,0,0,0,1,-1]

allcnt=0
def dfs(high,height,width,cnt):
    global allcnt
    tomatoes[high][height][width]=cnt
    cnt+=1
    if allcnt<cnt:
        allcnt=cnt
    for i in range(6):
        swidth=width+dm[i]
        sheight=height+dn[i]
        shigh=high+dh[i]
        if 0<=swidth<M:
            if 0<=sheight<N:
                if 0<=shigh<H:
                    if tomatoes[shigh][sheight][swidth]==0:
                        
                        
                        dfs(shigh,sheight,swidth,cnt)


for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k]==1:
                dfs(i,j,k,0)


flag=False

for i in range(H):
    for j in range(N):
        print(tomatoes[i][j])
        for k in range(M):
            
            if tomatoes[i][j][k]==0:
                flag=True

if flag:
    print(-1)
else:
    print(allcnt)






