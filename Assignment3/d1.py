 #find the frequency of every letter in a string using dictionary.
s=input("enter a string: ")
s=s.lower()
print(s)
thisdict={}
for i in s:
    if i not in thisdict:
        thisdict[i]=1
    else:
        thisdict[i]+=1
print(thisdict)
