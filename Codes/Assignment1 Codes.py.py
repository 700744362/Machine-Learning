print("question 1")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Min age = ",min(ages))
print("Max age = ",max(ages))
mid=int(len(ages)/2)
if(len(ages)%2==0):
    print("median age = ",(ages[mid]+ages[mid+1])/2)
else:
    print("median age = ",ages[mid])
print("Average age = ",(sum(ages)/len(ages)))
print("Range of Ages = ",max(ages)-min(ages))

print("\n")

print("Queestion 2")
dog={}
dog['name']="Charlie"
dog={'color':"Brown",'breed':"Lab",'legs':"medium",'age':3}
print(" Dog Dictionary after adding  key and value pairs = ")
print(dog)
student={}
student={'First_name':"Veerendra",'Last_name':"J",'Gender':"Male",'Age':22,'Martial_Status':"Single",'skills':["c"],'country':"Us",'city':"Kansas",'address':"OverlandPark"}
print("Length of Student dict = ",len(student))
print("Value of skills and Type of Skills in Student dict is \n ",(student['skills']),"\n ",type(student['skills']))
student['skills'].append("java")
student['skills'].append("Python")
print(student['skills'])
print(" List of Keys present in student dict are \n ",list(student.keys()))
print(" List of Values present in student dict are \n",list(student.values()))
      
print("\n")
      
print("Question 3")
brothers=("ajay","Ravi")
sisters=("julie",)
print("Values in tuple brothers = ",brothers," Sisters = ",sisters)
print(type(brothers),type(sisters))
siblings=(brothers+sisters)
print("Siblings = ",siblings)
print("I have ",len(siblings)," siblings")
a=list(siblings)
father={'Father_name':"Rao"}
a.append(father)
a.append("Lakshmi")
Family_members=tuple(a)
print("Family members",Family_members)
      
print("\n")
      
print("Question 4")

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Length of IT_Companies = ",len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update({"Infosys","TCS","Accenture"})
print(it_companies)
it_companies.remove("Google")
print(it_companies)
print("Union of A and B : \n",A.union(B))
print("Intersection of A and B : \n",A.intersection(B))
print("Is A Subset of B : ",A.issubset(B))
print("Are A and B disjoint Sets: ",A.isdisjoint(B))
AB=A.union(B)
print(" Join A with B : \n",AB)
print(" Join B with A : \n",B.union(A))
print("Symetric Difference between A and B : \n",A.symmetric_difference(B))
del A
del B
del it_companies
list_length=len(age)
age_Set=set(age)
set_length=len(age_Set)
print("Length of List = ",list_length,"\nLength of Set =",set_length)

print("\n")

print("Question 5")

radius=30
import  math as m
_area_of_circle_=m.pi*(radius**2)
print("Area of circle = ",_area_of_circle_)
_circum_of_circle_=2*m.pi*radius
print(" Circumference of circle = ",_circum_of_circle_)
radius=float(input("Enter radius of circle"))
_area_of_circle_=m.pi*(radius**2)
print("Area of circle = ",_area_of_circle_)

print("\n")

print("Question 6")

def Unique(w):
    for i in w:
        print(i)
string="I am a teacher and I love to inspire and teach people"
s1=set(string.split(" "))
Unique(s1)
print(" Number of Unique words = ",len(s1))

print("\n")

print("Question 7")
print("Name\tAge\tCountry\tCity\nAsabench\t250\tFinland\tHelsinki")

print("\n")
print("Question 8")
radius=10
area=3.14**2
print("The are of a circle with radius %d is %d meters square"%(radius,area))

print("\n")
print("Question 9")

n=int(input("Enter no of students"))
weights=[int(i) for i in input("Enter weights in lbs").split()]
kg=[]
for i in range(0,n):
    kg.append(weights[i]*0.453592)
print("Weights in Kilograms= \n",kg)




