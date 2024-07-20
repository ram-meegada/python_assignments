A=input("enter : ")
l=len(A)
count=0
for i in range(l):
    if(count==3):
        print(" ",end=" ")
        count=0
    print(A[i],end="")
    count=count+1