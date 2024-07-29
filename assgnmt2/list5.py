L = []
y = int(input("enter the length of the list : "))
for i in range(y):
    x = int(input("enter a number : "))
    L.append(x)
n = int((y/2)+1)
count = 0
for i in range(n):
    if(L[i] == L[(y-1)-i]):
        count = count+1
if(count == n):
    print("it is a palindrome")
else:
    print("it is not a palindrome")

