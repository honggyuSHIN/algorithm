import sys

# 거꾸로는 실패


input=sys.stdin.readline


N=int(input())

house=[]

for _ in range(N):
    house.append(list(map(int,input().split())))

visited={}
# (which,color) : cnt

def DP(which,color,cnt):


    # new color
    new=(color+1)%3
    new2=(color+2)%3


    # 할 놈만 DP함.
    if which-1>=0:
        if (which-1,new) in visited:
            if visited[(which-1,new)]>cnt:
                visited[(which-1,new)]=cnt
                DP(which-1,new,cnt+house[which-1][new])
        else:
            visited[(which-1,new)]=cnt
            DP(which-1,new,cnt+house[which-1][new])


        if (which-1,new2) in visited:
            if visited[(which-1,new2)]>cnt:
                visited[(which-1,new2)]=cnt
                DP(which-1,new2,cnt+house[which-1][new2])
        else:
            visited[(which-1,new2)]=cnt
            DP(which-1,new2,cnt+house[which-1][new2])


    

DP(N,0,house[N-1][0])
DP(N,1,house[N-1][1])
DP(N,2,house[N-1][2])

print(visited)


red=visited[(0,0)]
green=visited[(0,1)]
blue=visited[(0,2)]

print(red)
print(green)
print(blue)
print(min(red,green,blue))



    

