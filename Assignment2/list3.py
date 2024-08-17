#using ord() , encode() to generate ascii value of a alphabet.
#using chr()we can convert the ascii code to character.
l1=input("enter your name")
sum=0
for i in l1:
    sum += i.encode()[0]
    #sum += ord(i)
print("sum of the name: ",sum)

# convert the ascii
""" l=97
    print(chr(l))
"""


