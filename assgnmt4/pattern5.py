n=5
for i in range(1,n+1):
    k=1
    for j in range(i,n+1):
        if(j<=n):
            print(j,end=" ")
        else:
            print(k,end=" ")
            k+=1
    print("\n")
