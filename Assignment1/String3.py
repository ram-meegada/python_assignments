x=input("enter the String:")
#ln=x.split()
o=0
ln=[]
while(o<len(x)):
    intial=o
    if(x[o]==" "):
        pass

    o=o+1


l=len(ln)
k=[]
#l.reverse()
for i in range(l-1,-1,-1):
    k.append(ln[i])
#for i in range(len(l)-1,-1,-1):
#   print(l[i],end=" ")
#y=" ".join(k)
print(k)
y=""
for e in k:
    y +=" "+e
print(y)



# mango apple, banana,grapes