# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444
n = 6
k = (n*2)-1
l = []
l[0:k] = k*str(n)
m = []
i = 1
while i<=n:
    m.append("".join(l))
    z = n-i
    l[i:k-i] = (k-(2*i))*str(z)
    i = i+1
m = m+m[n-2::-1]
for i in m:
    print(i)