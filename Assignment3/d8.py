"""
input:a1b10
output:abbbbbbbbbb
"""
s=input("enter the string:")
t=""
for i in range(len(s)):
    if(s[i].isdigit()):
        t+=s[i]
    if(s[i].isalpha() or i==len(s)-1):
        if(i!=0):
            for k in range(int(t)):
                print(temp,end="")
            temp=""
            t=""
        temp=s[i]
    print("print",temp)
        
        
           
           
        
        

