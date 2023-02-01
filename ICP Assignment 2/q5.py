str=input("enter a string")
c1=0
c2=0
for i in str:
    if (i.isupper()):
        c1=c1+1
    elif (i.islower()):
        c2=c2+1
print("Upper case count = ",c1)
print("Lower case count = ",c2)
