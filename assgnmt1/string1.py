str1=input("enter a string : ")
str2=""
l=len(str1)
i=k=j=0
while(i<l):
    if(str1[i]==" "):
        i=i+1
        continue
    if(str1[i] not in str2):
        str2=str2+str1[i]
    i=i+1
print(str2)
m=len(str2)
for j in range(m):
    count=0
    for k in range(l):
        if(str2[j]==str1[k]):
            count=count+1
    print(str2[j],"=",count,end=" ")
