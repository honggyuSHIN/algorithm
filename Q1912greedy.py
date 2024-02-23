import sys

input=sys.stdin.readline

n=int(input())

cnt=0
startcnt=0
revercnt=0
idxcnt=0

li=list(map(int,input().split()))
flag=True
for i in range(n):
    
    if cnt+li[i]>0:
        cnt+=li[i]
        if flag:
            startcnt=i
            flag=False
        idxcnt=i
    else:
        cnt=0
        flag=True

print(f"cnt : {cnt}")

real=0
for i in range(idxcnt,startcnt,-1):
    
    revercnt+=li[i]
    if real>revercnt:
        real=revercnt
        print(f"real : {real}")

    


print(cnt-real)