s = "program"
n = len(s)
mid = n//2
r = s[mid:]+s[0:mid]
c=2*n
for i in range(n):
    c -= 2
    for j in range(c,0,-1):
        print(" ",end="")
    print(r[:i+1])