N=int(input())

li=[0]*46
li[0]=0
li[1]=1
li[2]=1

if N==1:
    print(1)
elif N==2:
    print(1)
else:
    for i in range(3,N+1):
        li[i]=li[i-1]+li[i-2]

    print(li[N])