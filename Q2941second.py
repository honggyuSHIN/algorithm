import sys

word=input()


li=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0
subcnt=len(word)
for i in li:
    if i=='z=':
        a=word.count(i)-word.count('dz=')
    else:
        a=word.count(i)
    cnt+=a
    if len(i)==2:
        subcnt-=2*a
    else:
        subcnt-=3*a
cnt+=subcnt

print(cnt)













