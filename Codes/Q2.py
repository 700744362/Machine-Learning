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
      
