n=4
s1=[]
i,j,l=-1,(2*n)-1,n+1
for i1 in range((2*n)-2):
    if(i1<n):
        i+=1
        j-=1
        l-=1
    else:
        i-=1
        j+=1
        l+=1
    s1[i:j+1]=str(l)*(j+1-i)
    print("".join(s1))


    

