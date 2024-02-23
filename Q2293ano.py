import sys

n, k = map(int, sys.stdin.readline().split())
a = [0] * 1001
d = [1] * 1001

for i in range(1,n+1):
    a[i] = int(sys.stdin.readline())

d[0] = 1

for i in range(1,n+1):
    for j in range(a[i],k+1):              
        d[j] += d[j - a[i]]
        
print(d[k])


'''
1 10000

1

'''




'''
D(n, k) : n가지의 동전으로 k원을 만들 수 있는 경우의 수

n가지의 동전으로 k원을 만들기 위해서

(1) Cn 동전을 쓰지 않고 k원을 만든 경우 : N(n-1, k)

(2) Cn 동전을 1개라도 써서 k원을 만든 경우 : N(n, k-Cn)

D(n, k) = (1) + (2) = D(n-1, k) + D(n, k-Cn)

가 도출된다고 하는데.. (2)번 과정이 이해가 안가네요. 고수님들 설명좀 부탁드려요~




이 문제에서는 같은 종류의 동전을 몇 번을 사용해도 상관없다고 했기 때문에 n번째 
동전을 한번 사용했다는 상태를 나타낸 거에요.

만약, 최대 한번 사용가능하다고 하면, D(n,k) = D(n-1,k) + D(n-1,k-Cn) 이 되겠져




D(n,k) = D(n-1,k) + D(n,k-Cn)이 여러번 처리를 해줄 수 있어요.

D(n,k) -> D(n,k-Cn) -> D(n, k-Cn-Cn) -> D(n, k-Cn-Cn-Cn) ... n번째를 더 이상 사용하지 않는 경우는

-> D(n-1, k-Cn-Cn-Cn) 으로 나타날수 있어여



'''