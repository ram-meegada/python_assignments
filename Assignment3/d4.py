#sort the dictionary by keys and values.
d={'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}
key=list(d.keys())
duple_key=list(d.keys())
value=list(d.values())
duple_value=list(d.values())
key.sort()
value.sort()
d1={k:d[k] for k in key}
d2={}
j=0
for l in value:
   for h in range(len(duple_value)):
      if(l==duple_value[h]):
         d2[duple_key[h]]=l


print("using keys as a sorting factor:",d1)
print("using values as a sorting factor:",d2)
