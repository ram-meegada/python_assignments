L1 = []
L2 = []
L3 = []
y = int(input("enter the length of the list : "))
for i in range(y):
    x = int(input("enter a number : "))
    a = int(input("enter a number : "))
    L1.append(x)
    L2.append(a)
print(L1,L2)
for i in range(y):
    z = L1[i]+L2[y-1-i]
    L3.append(z)
print(L3)