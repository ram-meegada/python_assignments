"""Write a Python program to get the top three items in a shop.
   Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
   Expected Output:
   item4 55
   item1 45.5
   item3 41.3"""
d= {'item1': 0, 'item2': -2, 'item3': -3, 'item4': -1, 'item5': 1}
for i in range(3):
    d1=list(d.items())
    max_val=d1[0][1]
    #print("print",max_val)
    max_key=d1[0][0]
    for k,v in d.items():
        if(v>max_val):
            max_val=v
            max_key=k
    print(d)
    print(max_key," ",max_val)
    d.pop(max_key)