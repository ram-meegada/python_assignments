# Write a Python program to get the top three items in a shop.
#    Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#    Expected Output:
#    item4 55
#    item1 45.5
#    item3 41.3
d = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
g = sorted(d.items(), key=lambda f:f[1])
print(g[-1:-4:-1])