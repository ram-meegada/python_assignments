#                 1
#               2 4
#             3 5 7
#         6 8 10 12
#     9 11 13 15 17
# 14 16 18 20 22 24
n = 25
o = 1
e = 2
l = []
s = ""
for i in range(1,n+1):
    for j in range(i):
        if(i%2==1):
            s = s+str(o)+" "
            o = o+2
        else:
            s =s+str(e)+" "
            e = e+2
    l.append(s)
    s = ""

q = (len((l[n-1])))-1
for a in range(0,n):
    r = (len(l[a]))-1
    print((q-r)*"a",end="")
    print(l[a])