import sys

input=sys.stdin.readline

n,k=map(int,input().split())

candi=[]

for _ in range(n):
    candi.append(int(input()))


ans=[0]*(k+1)
ans[0]=1

for i in candi:
    for j in range(i,k+1):
        ans[j]+=ans[j-i]


print(ans[k])
'''

0   1   2   3   4   5   6   7   8   9   10
    1   2   3   4   5   6   7   8   9   10



'''





