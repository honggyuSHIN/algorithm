import sys
input=sys.stdin.readline

N=int(input())

cnt=0

all=N//5

flag=False
for i in range(all,0,-1):
    temp=N-(5*i)
    if temp%3==0:
        cnt+=i
        N-=(5*i)
        flag=True
        break

if N%3==0:
    cnt+=(N//3)
else:
    cnt=-1
print(cnt)










