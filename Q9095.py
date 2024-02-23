import sys
input=sys.stdin.readline

n=int(input())

D=[0]*12
D[1]=1
D[2]=2
D[3]=4
# 3     111     12
def DP(k):
    if k<=3:
        print(D[k])
        return
    
    for i in range(4,k+1):
        D[i]=D[i-3]+D[i-2]+D[i-1]
    print(D[k])

for _ in range(n):
    k=int(input())
    DP(k)



'''

w   0   1   2   3   4   5   6   7   8   9   10
1   1   1   1   1   1   1   1   1   1   1   1                          
2   1   1   2   2   3   4   5   6   7   8   9            
5   1                                  


'''






