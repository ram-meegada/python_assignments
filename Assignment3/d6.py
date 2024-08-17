"""
 Write a Python program to print all distinct values in a dictionary.
   Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
   Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique=[]
for i in d:
    x=list(i.values())
    if(x[0] not in unique):
        unique.append(x[0])
print(unique)