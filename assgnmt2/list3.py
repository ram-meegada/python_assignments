d = input("enter : ")
k = list(d)
x = y = 0
#using encode() string method
for i in k:
    x = x+i.encode()[0]
#using ord() to get the ascii value of a character
for j in k:
    y = y+ord(j)
print(x)
print(y)
