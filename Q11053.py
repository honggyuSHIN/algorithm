import sys

input=sys.stdin.readline

N=int(input())


li=list(map(int,input().split()))

answer=[1]*N


for i in range(1,N):
    for j in range(i):
        if li[i]>li[j] and answer[i]<answer[j]+1:

            answer[i]=answer[j]+1



print(max(answer))




'''

7
5 1 2 3 4 10 20

'''


