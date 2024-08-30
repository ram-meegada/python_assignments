# 4 4 4 4
# 4 3 3 4
# 4 3 3 4
# 4 4 4 4

n = 6
k = n//2
l = []
m = []
l[0:n] = n*str(n)
i = 1
while i<=k:
    m.append("".join(l))
    y = n-i
    l[i:n-i] = (n-(2*i))*str(y)
    i = i+1
print(m,"-------")
m = m+m[k-1::-1]
for i in m:
    print(i)