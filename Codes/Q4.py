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
