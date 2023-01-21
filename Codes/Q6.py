print("Question 6")

def Unique(w):
    for i in w:
        print(i)
string="I am a teacher and I love to inspire and teach people"
s1=set(string.split(" "))
Unique(s1)
print(" Number of Unique words = ",len(s1))
