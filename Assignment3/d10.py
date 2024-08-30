s ="""Technology has had a profound impact on society"""

temp={1:2,2:4,3:8,4:12}
l=[]
key=1
r=0
# for i in temp.values():
#     s1=s[r:r+i]
#     l.append(s1)
#     r+=i
# x=val.pop()
# while(r<len(s)):
#     s1=s[r:r+x] 
#     l.append(s1)
#     r+=i

# print(l)
while(r<len(s)):
    l.append(s[r:r+temp[key]])
    r += temp[key]
    if(key < len(temp)):
        key += 1
print(l)

    

