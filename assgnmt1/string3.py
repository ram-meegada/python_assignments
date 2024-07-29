X=input("enter : ")
n=len(X)
L=[]
m=0
for i in range(n):
    if(X[i]==" "):
        L.append(X[m:i])
        m=i+1
    elif(i==(n-1)):
        L.append(X[m:])
    else:
        pass
print(L)
i=len(L)-1
#print(Y)
while(i>=0):
    print(L[i],end=" ")
    i=i-1

