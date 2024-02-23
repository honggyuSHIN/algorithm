



'''

10
0    10 -4 3 1 5 6 -35 12 21 -1


'''


import sys
input=sys.stdin.readline

n=int(input())

li=list(map(int,input().split()))
cnt=0
best=-10*5
for i in li:
    cnt=max(cnt+i,i)
    best=max(best,cnt)
print(best)