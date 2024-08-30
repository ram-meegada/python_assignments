#    1
#   1 1
#  1 2 1  
# 1 3 3 1
#1 4 6 4 1
n = 7
for i in range(n):
    print(" "*(n-(i+1)),end="")
    u = str(11**i)
    for i in u:
        print(i,end=" ")
    print()