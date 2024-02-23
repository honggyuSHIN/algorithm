number=int(input())
li=list(map(int,input().split()))



def insert(li):
    for i in range(number):
        for j in range(i-1,-1,-1):
            if li[j]<li[i]:
                temp=li[i]
                del li[i]
                li.insert(j+1,temp)
                break
            if j==0:
                temp=li[i]
                del li[i]
                li.insert(0,temp)
                


def bubble(li):
    for j in range(len(li)-1):
        for i in range(len(li)-1):
            if li[i]>li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]



def selection(li):
    for i in range(len(li)):
        temp=min(li[i:len(li)])
        tempindex=li[i:len(li)].index(temp)+i
        print(temp,tempindex)
        li[i],li[tempindex]=li[tempindex],li[i]
        print(li)
    
insert(li)
print(li)

s=[0]*number
s[0]=li[0]

for i in range(1,number):
    s[i]=s[i-1]+li[i]

print(sum(s))

    


# length=len(li)
# total=0
# for i in li:
#     total+=i*length
#     length-=1
# print(total)








