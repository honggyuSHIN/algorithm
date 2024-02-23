li=list(map(int,input().split()))
condi=[1,1,2,2,2,8]
answer=[]
for i in range(len(li)):
    a=condi[i]-li[i]
    answer.append(a)

for i in answer:
    print(i,end=' ')