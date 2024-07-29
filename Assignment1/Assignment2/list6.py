s=input("enter the string:")
s1=input("enter the word to check:")
l=len(s1)
flag=0
for i in range(len(s)):
    if(s[i]==s1[0]):
        if(s[i:i+l]==s1):
            print("index starts from ",i,(i+l-1))
            flag=1
            
if(flag==0):
    print("element not found!!")
        