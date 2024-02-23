import sys
input=sys.stdin.readline

k=int(input())

li=[]

for _ in range(k):
    number=int(input())
    if number!=0:
        li.append(number)
    elif number==0:
        li.pop()    

print(sum(li))











