# convert list of lists to dictionary.
L=[["name","emmy",89],["age",12,"ford"],["list",True]]
dict1={}
for i in L:
    dict1[i[0]]=i[1]
print(dict1)
    

