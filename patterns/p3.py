n=6
e=2
o=1
if(n==2):
    s=2
elif(n>=3):
    s=4*(n-2)
for i in range(1,n+1):
    if(s>12):
        for j in range(s):
            print(" ",end="")
        s-=2
    elif(s<=12):
        for j in range(s):
            print(" ",end="")
        s-=4
    
    for k in range(0,i):
        if(i%2!=0):
            print(o,end=" ")
            o+=2
        else:
            print(e,end=" ")
            e+=2
    print()

    


