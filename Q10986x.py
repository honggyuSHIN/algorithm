import sys
input=sys.stdin.readline


n,m=map(int,input().split())

li=list(map(int,input().split()))
li02=[]
total=0
for i in li:
    total+=i
    li02.append(total)
cnt=0
for i in li02:
    if i%m==0:
        cnt+=1
for i in range(0,len(li02)):
    for j in range(i+1,len(li02)):

        if (li02[j]-li02[i])%m==0:
            cnt+=1

print(cnt)
