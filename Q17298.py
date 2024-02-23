from collections import deque
length=int(input())
li=list(map(int,input().split()))
lisave=[0 for i in range(len(li))]
ans=[0]*length

mydeque=deque()

for i,j in enumerate(li):
    # 덱에 아무것도 없을 때
    if len(mydeque)==0:
        mydeque.append([i,j])
    # 덱에 뭐가 있을 때 마지막 것 확인.
    else:
        # j보다 작은 놈들 다 지정해줬음
        while(mydeque and mydeque[-1][1]<j):
            lisave[mydeque[-1][0]]=j
            mydeque.pop()
    # 지정 다 해주고 들어감.
    mydeque.append([i,j])

# 마지막 남은 하나 지정
for i in mydeque:
    lisave[i[0]]=-1



for i in lisave:
    print(i,end=" ")




















    # flag=True
    # for k in range(i+1,len(li)):
    #     if j<li[k]:
    #         print(li[k])
    #         deque.append([i,j])
    #         flag=False
    #         break
    # if flag:
    #     print(-1)




