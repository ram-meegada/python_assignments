l1=[]
l=int(input("enter the length of the list"))
for i in range(l):
    print("enter",i,"element",end=" ")
    x=int(input())
    l1.append(x)
i=1
j=0
while(i<l):
    key=l1[i]
    j=i-1
    while(j>=0):
        if(l1[j]>key):
            temp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
        j-=1
    i+=1
print("the second largest number is:",l1[-2])