#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1
n = 7
for i in range(n):
    print((n-i-1)*" ",end="")
    for j in range(i+1,0,-1):
        print(j, end="")
    print()