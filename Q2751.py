import sys
input=sys.stdin.readline

n=int(input())
li=[]


for i in range(n):
    temp=int(input())
    li.append(temp)

def merge(li):
    if len(li)==1:
        return li
    start=0
    end=len(li)-1
    midium=int((start+end)/2)+1
    answer=[]
    li01=merge(li[:midium])
    li02=merge(li[midium:])

    while len(li01)>0 and len(li02)>0:
        if li01[0]==li02[0]:
            answer.append(li01[0])
            li01.pop(0)
            li02.pop(0)
        elif li01[0]>li02[0]:
            answer.append(li02[0])
            li02.pop(0)
        else:
            answer.append(li01[0])
            li01.pop(0)

    for i in li01:
        answer.append(i)
    for i in li02:
        answer.append(i)
    return answer

li=merge(li)

for i in li:
    print(i)














