'''
3
0 1 0
0 0 1
1 0 0


0-1
1-2
2-0


'''



import sys
from collections import deque
input=sys.stdin.readline

N=int(input())

table=[[]for _ in range(N)]


for i in range(N):
    li=list(map(int,input().split()))
    for j in range(N):
        if li[j]==1:
            table[i].append(j)






def find(i,j):
    q=deque()
    check=set()

    q.extend(table[i])

    while q:
        temp=q.popleft()

        if temp in check:
            continue
        check.add(temp)

        if temp==j:
            return True
        q.extend(table[temp])




for i in range(N):

    for j in range(N):

        if find(i,j)==True:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()


