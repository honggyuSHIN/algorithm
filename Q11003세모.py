


# 12 7
# 1 5 2 3 6 2 3 7 3 5 2 6

# 1 1 1 2 2 2 2 2 3 3 2 2


# n : 전체 개수, m : 특정 개수

'''
덱(리스트)을 만들어서 하나씩 뒤에 추가함.
추가되는 것들 보다 값이 큰 것들은 지워도 됨. 가장 최근에 추가된 게 더 오래
남아 있으니까.

allcnt, allminuscnt 갱신하고
enumerate 써서 값하고 인덱스 같이 추가해서 값을 기준으로 지울 거 지움
-> 작은 순서대로 남아있음.

최소값 확인할 때에는 인덱스 allcnt, allminuscnt 확인해서 범위 안에 안 들면 지우고
범위 안에 들면 최소값 출력


'''
import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))
mydeque=deque([[0,li[0]]])

allcnt=0
allminuscnt=0-m+1


for i,j in enumerate(li):
    
    # mydeque에 첨가.
    # 지우기
    while  mydeque and mydeque[-1][1]>=j:
        mydeque.pop()
    
    mydeque.append([i,j])
    

    # 출력
    # cnt값 조정
    if allminuscnt<0:
        cnt=0
    else:
        cnt=allminuscnt
    # 왼쪽부터 최소값 출력. 인덱스 확인해야 함.
    dequecnt=0
    while mydeque[0][0]<cnt:
        mydeque.popleft()
    print(mydeque[0][1])


    allcnt+=1
    allminuscnt+=1




        
    # for i in mydeque:
    #     if i[0]<cnt:
    #         continue
    #     print(i[1])
        # break


