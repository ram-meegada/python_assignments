l1=[]
l=int(input("enter the length of the list"))
for i in range(l):
    print("enter",i,"element",end=" ")
    x=int(input())
    l1.append(x)
flag=0
for i in range(int(l/2)):
    if(l1[i]!=l1[l-1-i]):
        flag=1
        break
if(flag==0):
    print("true")
else:
    print("false")