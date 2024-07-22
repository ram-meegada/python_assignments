""""F=input("enter : ")
n=len(F)
min=0
temp=""
for i in range(n-1):
    min=i
    if(F[i]==" "):
        continue
    for j in range(i+1,n):
        if(F[j]==" "):
            continue
        if(F[j]<F[min]):
            min=j
    if(i!=min):
       temp=F[i]
       F=F[:i]+F[min]+F[i+1:min]+temp+F[min+1:]
for i in range(n):
    if(F[i]==" "):
        continue
    print(F[i],end="")"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.append(list1)
print(list1)

       