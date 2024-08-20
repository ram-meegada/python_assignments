A = "SREEhdhhdyheydn"
d = {}
for i in A:
    if i not in d:
        d[i] = 1
    elif i in d:
        d[i] += 1 
print(d)