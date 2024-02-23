import sys
input=sys.stdin.readline
li=[]
for _ in range(5):
    li.append(input())
answer=''
for i in range(16):
    for j in li:
        try:
            answer+=j[i]
        except:
            pass
answer=answer.replace('\n','')
print(answer)
