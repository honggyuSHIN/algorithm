# 특정 경우에 오류가 생기는 것 같음.

import sys

input=sys.stdin.readline

result=0

n=int(input())
li=list(map(int,input().split()))

temp=[0]*(n)


 
def merge_sort(s,e):

    if e-s==0:
        return
    global result

    m=int(s+(e-s)/2)

    # 함수를 다시 호출하는 게 구간을 나눠주는 역할 밖에 안 됨.
    merge_sort(s,m)
    merge_sort(m+1,e)


    index01=s
    index02=m+1
    k=s
    # 3 5 7     2 6 5 2

    while index01<=m and index02<=e:
        if li[index01]<li[index02]:
            temp[k]=li[index01]
            index01+=1
        else:
            temp[k]=li[index02]
            index02+=1
            result+=(m-index01+1)
        k+=1
    # 둘 중에 남은 거 짜내기
    while index01<=m:
        temp[k]=li[index01]
        index01+=1
        k+=1
            
    while index02<=e:
        temp[k]=li[index02]
        index02+=1
        k+=1

    for i in range(s,e+1):
        li[i]=temp[i]
    

merge_sort(0,len(li)-1)

print(result)











# def merge_sort(li):
#     global allcnt
#     if len(li)==1:
#         return li
        
#     median=int(len(li)/2)
#     front=merge_sort(li[:median])
#     back=merge_sort(li[median:])

#     reli=[]
#     while len(front)!=0 and len(back)!=0:
#         if front[0]<back[0]:
#             reli.append(front[0])
#             front.pop(0)
#             allcnt+=1
#         else:
#             reli.append(back[0])
#             back.pop(0)
#             allcnt+=1

        
#     for i in front:
#         reli.append(i)
#     for i in back:
#         reli.append(i)
    
#     return reli

# merge_sort(li)
# print(allcnt)
























