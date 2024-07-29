x = input("enter : ")
y = input("substring : ")
n = len(x)
for i in range(n):
    #print(x[i:i+2])
    if(y == x[i:i+2]):
        print("index is from : ",i,i+1)
        