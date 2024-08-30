#       *
#     * * *
#   * * * * *
# * * * * * * *
n = 4
c = n
for i in range(n):
    for j in range((2*c)-1):
        print(" ", end = "")
    for k in range((2*i)+1):
        print("* ", end = "")
    print("\n")
    c -= 1