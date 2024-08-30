n=7
for i in range(0,n):
    for j in range(i+1,n+i+1):
        if(j<=n):
            print(j,end="")
        else:
            print(j-n,end="")
    print()