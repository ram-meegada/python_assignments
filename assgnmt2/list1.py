L = []
y = int(input("enter the length of the list : "))
for i in range(y):
    x = int(input("enter a number : "))
    L.append(x)
m = 0
j = 1
for i in range(1,y):
    for j in range(i):
        if(L[j]<L[i]):
            temp = L[j]
            L[j] = L[i]
            L[i] = temp
print(L)
print("the second largest element of the list is : ",L[1])
