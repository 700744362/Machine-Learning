print("question 1")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Min age = ",min(ages))
print("Max age = ",max(ages))
ages.append(min(ages))
ages.append(max(ages))
mid=int(len(ages)/2)
if(len(ages)%2==0):
    print("median age = ",(ages[mid]+ages[mid+1])/2)
else:
    print("median age = ",ages[mid])
print("Average age = ",(sum(ages)/len(ages)))
print("Range of Ages = ",max(ages)-min(ages))
