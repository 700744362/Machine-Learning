for i in range(5):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")
for i in range(1,5):
    for j in range(i,5):
            print("*",end=" ")
    print("\n")
    
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(0,len(my_list)):
    if i%2==1:
        print(my_list[i],end=" ")
print("\n")

x = [23, "Python", 23.98]
for i in range(0,len(x)):
    x.append(type(x[i]))
print(x)
print("\n")

sl= [1,2,3,3,3,3,4,5]
ul=list(set(sl))
print(ul)
print("\n")

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
