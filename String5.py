p=input("enter the String:")
o=""
for k in p:
    if(k.isalpha()):
        o=o+k
length=len(o)
x=list(o)

for i in range(1,length):
    key=x[i]
    for j in range(i-1,-1,-1):
        if(key<x[j]):
            temp=x[j]
            x[j]=key
            x[j+1]=temp
            
print("".join(x))


