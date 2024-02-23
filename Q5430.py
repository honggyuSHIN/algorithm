import sys
input=sys.stdin.readline
# 시간 초과

n=int(input())
solve=[]
for i in range(n):
    question=[]
    func=input()
    length=int(input())
    li=input()
    solve.append([func,length,li])

func=func.replace('RR','')

for i in solve:
    func=i[0]
    length=i[1]
    li=i[2]

    if len(li)==3:
        li=[]
    else:
        li=list(map(int,li[1:-2].split(',')))


    flag=True
    for i in func:
        
        if i=="R":
            li=li[::-1]
        elif i=="D":
            if len(li)==0:
                print("error")
                flag=False
                break
            else:
                li.pop(0)
    if flag:
        print(li)