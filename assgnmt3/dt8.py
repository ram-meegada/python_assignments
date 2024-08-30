# input:a1b2
# output:abb
i = "a5b3"
a = list(i[1::2])
b = list(i[0::2])
for j in range(len(a)):
    print(int(a[j])*b[j],end="")
