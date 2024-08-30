#  Write a Python program to print all distinct values in a dictionary.
#    Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#    Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
d =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
s = []
for i in d:
    v = list(i.values())
    if v[0] not in s:
        s.append(v[0])
print(s)