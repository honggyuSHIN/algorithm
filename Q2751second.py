import sys
input=sys.stdin.readline


n=int(input())

li=[]
for i in range(n):
    li.append(int(input()))

temp=[0 for i in range(len(li))]

def merge(start,end):
    if start==end:
        return
    mid=int((start+end)/2)
    # 0,1 -> 0
    # 0 2 -> 1
    # 1,2 -> 1

    merge(start,mid)
    merge(mid+1,end)

    index01=start
    index02=mid+1
    k=start
    
    while index01<=mid and index02<=end:
        
        if li[index01]==li[index02]:
            temp[k]=li[index02]
            index01+=1
            index02+=1

        elif li[index01]>li[index02]:
            temp[k]=li[index02]
            index02+=1

        elif li[index01]<li[index02]:
            temp[k]=li[index01]
            index01+=1
        k+=1

    while index01<=mid:
        temp[k]=li[index01]
        index01+=1
        k+=1

    while index02<=end:
        temp[k]=li[index02]
        index02+=1
        k+=1

    
    # temp를 다시 li로 돌려보내기. 갱신해야 함.
        
    for i in range(start,end+1):
        li[i]=temp[i]
    


merge(0,len(li)-1)

for i in li:
    print(i)

















