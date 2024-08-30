# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 4 3 2 1
n = 7
for j in range(n):
    for k in range(j,n):
        print(k+1,end=" ")
    for i in range(j):
        print(i+1,end=" ")
    print()