
class Student():
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ("The student new name is ", name, "and his age is", age)
    def addme (self, tracks):
        self.tracks = tracks
        print ("His new track is ", tracks)
    def student_score(self, score):
        self.score = 80
        print("The student score is", "80")
       



#calling a class
s = Student("Sia",74)
print (s.addme("UI"))
print (s.student_score(80))





