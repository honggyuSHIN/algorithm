import sys

input=sys.stdin.readline


n=int(input())



def DP(k):
    global cnt
    if k<0:
        return
    elif k==0:
        cnt+=1
    else:
        DP(k-1) 
        DP(k-2)
        DP(k-3)



for _ in range(n):
    cnt=0
    k=int(input())
    DP(k)
    print(cnt)









