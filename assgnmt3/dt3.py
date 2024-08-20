# Given a list and dictionary, map each element of list with each item of dictionary, forming nested dictionary as value
#    The original dictionary is : {'Gfg': 4, 'is': 5, 'best': 9}
#    The original list is : [8, 3, 2]
#    The mapped dictionary : {8: {'Gfg': 4}, 3: {'is': 5}, 2: {'best': 9}}

d = {'Gfg': 4, 'is': 5, 'best': 9}
l= [8, 3, 2]
c = 0
md = {}
for x,y in d.items():
    md[l[c]]={x:y}
    c += 1
print(md)
