t=int(input())
li=[]
for i in range(t):
    n,m=map(int,input().split())
    li.append([n,m])


# m이 더 큼.
def gcd(n,m):
    if n>m:
        n,m=m,n
    if n==1:
        return n
    elif m==1:
        return m
    
    a=m%n
    if a==0:
        return n
    else:
        return gcd(n,a)


for n,m in li:
    a=gcd(n,m)
    print(int((n*m)/a))

