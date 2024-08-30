# sort the dictionary by keys and values
d = {3: 5, 9: 2, 8: 2}
a = {i:j for i,j in sorted(d.items(), key=lambda j:j[1])}
print(a)
b = {i:j for i,j in sorted(d.items())}
print(b)