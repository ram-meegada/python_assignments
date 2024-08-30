s = "pattern"
mid=(len(s)-1)//2
new=s[mid:len(s)]+s[:mid]
k=0
v = (len(s)-1)*2
for i in  range(v,-1,-2):
    print("*"*v,end="")
    k+=1
    v -= 2
    print(new[0:k])