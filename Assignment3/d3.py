"""
 Given a list and dictionary, map each element of list with each item of dictionary, forming nested dictionary as value
   The original dictionary is : {'Gfg': 4, 'is': 5, 'best': 9}
   The original list is : [8, 3, 2]
   The mapped dictionary : {8: {'Gfg': 4}, 3: {'is': 5}, 2: {'best': 9}}
"""
dict1 = {'Gfg': 4, 'is': 5, 'best': 9}
item = list(dict1.items())
print(item)
list1 =  [8, 3, 2]
map = {}
k = len(dict1)
a = 0
for i,j in dict1.items():
    map[list1[a]] = {i:j}
    a += 1
print(map)