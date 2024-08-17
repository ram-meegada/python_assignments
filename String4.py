x=input("enter the String:")
count=0
for i in x:
    if(count<3):
        count=count+1
       
    else:
        count=0
        print(",",end="")
        count=count+1
    print(i,end="")    

