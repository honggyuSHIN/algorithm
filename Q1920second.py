import sys
input=sys.stdin.readline


N=int(input())
li=set(input().strip().split())

M=int(input())
candi=list(input().strip().split())



for i in candi:
    if i in li:
        print(1)
    else:
        print(0)





