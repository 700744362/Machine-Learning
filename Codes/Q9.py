print("Question 9")

n=int(input("Enter no of students"))
weights=[int(i) for i in input("Enter weights in lbs").split()]
kg=[]
for i in range(0,n):
    kg.append(weights[i]*0.453592)
print("Weights in Kilograms= \n",kg)
