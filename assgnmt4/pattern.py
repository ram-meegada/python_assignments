o = "123456789"
n = len(o)
for i in range(0,n//2):
    print(2*i*" ",end="")
    print(o[i], end="")
    for l in range((2*len(o[i+1:n-i-1]))+1):
        print(" ",end="")
    print(o[n-i-1])
print((2*(n//2))*" "+o[n//2])
for j in range((n//2)-1,-1,-1):
    print(2*j*" ",end="")
    print(o[j],end="")
    for k in range((2*len(o[j+1:n-j-1]))+1):
        print(" ", end="")
    print(o[n-j-1])