import sys

input=sys.stdin.readline

N=int(input())
li=list(input().strip().split())

M=int(input())
candi=list(input().strip().split())


li.sort()




def binary(i,start,end):
    global flag
    if start==end:
        if li[start]==i:
            flag=True
        return


    medium=int((start+end)/2)

    if li[medium]==i:
        flag=True
    else:
        binary(i,start,medium)
        binary(i,medium+1,end)    

start=0
end=len(li)-1

for i in candi:
    flag=False
    binary(i,start,end)
    if flag:
        print(1)
    else:
        print(0)














