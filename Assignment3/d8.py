s = "a1c2b5"
t=""
for i in range(len(s)):
    if(s[i].isdigit()):
        t+=s[i]
    if(s[i].isalpha() or i==len(s)-1):
        if(i!=0):
            print(int(t)*temp,end="")
            temp=""
            t=""
        temp=s[i]