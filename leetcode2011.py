def increment(x):
    x+=1
    return x
  
def decrement(x):
    x-=1
    return x

x=0
l= ["--X","X++","X++"]

for i in l:
    if "++" in i:
        x=increment(x)
  
    elif "--" in i:
        x=decrement(x)

print(x)

