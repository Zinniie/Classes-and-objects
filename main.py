
class Bob():
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ("name= ", name)
        print ("age=", age)
    def addme (self, tracks):
        self.tracks = tracks
        print ("track= ", tracks)
    def Bob_score(self, score):
        self.score = 80
        print("score=", "80")
       



#calling a class
Bob = Bob("Sia",74)
print (Bob.addme("UI"))
print (Bob.Bob_score(80))





