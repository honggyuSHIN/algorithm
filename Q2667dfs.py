
N=int(input())

li=[[]for i in range(N+1)]

for i in range(N+1):
    li[0].append(0)
for i in range(1,N+1):
    li[i].append(0)
    li[i].extend(list(map(int,input())))


# 인덱스 1~N 신경쓰면 됨.


cntsave=[]

cnt=0

# 인수 전달 받아서 하는 건 왜 안 되는지 생각해볼 것.

def dfs(y,x):
    global cnt
    if y==0 or y>N or x==0 or x>N:
        return
    if li[y][x]==0:
        return
    li[y][x]=0

    cnt+=1
    dfs(y-1,x)
    dfs(y,x-1)
    dfs(y+1,x)
    dfs(y,x+1)
    return 
    
    
allcnt=0
for i in range(1,N+1):
    for j in range(1,N+1):
        if li[i][j]==1:
            a=dfs(i,j)
            cntsave.append(cnt)
            cnt=0
            allcnt+=1



print(allcnt)

cntsave.sort()
for i in cntsave:
    print(i)


# for i in range(N+1):
#     print(li[i])








