l1=[]
l=int(input("enter the length of the list"))
for i in range(l):
    print("enter",i,"element",end=" ")
    x=int(input())
    l1.append(x)
l2=l1[-1::-1]
if(l2==l1):
    print("it is palindrome")
else:
    print("it is not palindrome")