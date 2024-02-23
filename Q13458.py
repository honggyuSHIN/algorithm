import sys
input=sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
B,C=map(int,input().split())

cnt=0

for i in li:
    temp=i
    if i==0:
        continue
    # main
    temp-=B
    cnt+=1

    # sub
    while temp>0:
        a=int(temp/C)
        if temp%C==0:
            cnt+=a
        else:
            cnt+=(a+1)
        break
print(cnt)
