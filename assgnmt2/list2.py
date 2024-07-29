t = input("enter : ")
for i in t:
    if(i == " "):
        continue
    elif((ord(i) >= 65)and(ord(i) <= 90)):
        print(i,end = "")
    else:
        pass