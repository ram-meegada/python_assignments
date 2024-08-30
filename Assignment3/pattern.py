'''
    give the even length :
    4444
    4334
    4334
    4444
'''
k=8
s1=[]
i,j,l=-1,k,k+1
for i1 in range(k-1):
    if(i1<(k/2)):
        i+=1
        j-=1
        l-=1
    else:
        i-=1
        j+=1
        l+=1
    s1[i:j+1]=str(l)*(j+1-i)
    print("".join(s1))
    if(i1+1==(k/2)):
        print("".join(s1))

