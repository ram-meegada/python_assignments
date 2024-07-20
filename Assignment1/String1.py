s=input("enter the string: ")
str=set(s)
for i in str:
    if(i!=" "):
        print(i ,"-" ,s.count(i),end=" ")

