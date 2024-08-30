""""
given a odd length word which should be printed from the middle of the word"""
s=input("enter a odd length string:")
mid=(len(s)-1)//2
new=s[mid:len(s)]+s[:mid]
k=0
v=(len(s)*2)
for i in  range(v,1,-2):
    print("print",i)
    print("a"*i,end="")
    k+=1
    print(new[0:k])