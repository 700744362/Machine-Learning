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
