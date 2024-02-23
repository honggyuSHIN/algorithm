from collections import deque
import copy

# https://leeingyun96.tistory.com/22
# dp 배운 후에 다시 해볼 것.

R,C=map(int,input().split())

# 세로 R, 가로 C

alphabet=[[]for _ in range(R+1)]

alphabet[0]=[0]*(C+1)

for i in range(1,R+1):
    alphabet[i].append(0)
    alphabet[i].extend(list(input()))
 
# li = [list(input()) for _ in range(n)]
    
# 1-R       / 1-C


dr=[1,-1,0,0]
dc=[0,0,1,-1]

check=""
q=deque()

cnt=0
def bfs(r,c,check):
    global cnt

    q.append((r,c,check))

    while q:
        r,c,check=q.popleft()
        check+=alphabet[r][c]
        if cnt<len(check):
            cnt=len(check)
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if 1<=nr<=R and 1<=nc<=C:
                if alphabet[nr][nc] not in check:
                    q.append((nr,nc,check))



bfs(1,1,check)

print(cnt)




'''
20 20
ABCDEFGHIJKLMNOPQRST
BCDEFGHIJKLMNOPQRSTU
CDEFGHIJKLMNOPQRSTUV
DEFGHIJKLMNOPQRSTUVW
EFGHIJKLMNOPQRSTUVWX
FGHIJKLMNOPQRSTUVWXY
GHIJKLMNOPQRSTUVWXYZ
HIJKLMNOPQRSTUVWXYZZ
IJKLMNOPQRSTUVWXYZZZ
JKLMNOPQRSTUVWXYZZZZ
KLMNOPQRSTUVWXYZZZZZ
LMNOPQRSTUVWXYZZZZZZ
MNOPQRSTUVWXYZZZZZZZ
NOPQRSTUVWXYZZZZZZZZ
OPQRSTUVWXYZZZZZZZZZ
PQRSTUVWXYZZZZZZZZZZ
QRSTUVWXYZZZZZZZZZZZ
RSTUVWXYZZZZZZZZZZZZ
STUVWXYZZZZZZZZZZZZZ
TUVWXYZZZZZZZZZZZZZZ


'''