#created class as student
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
          self.name = str (name)
          self.age = int (age)
          self.tracks = list (tracks)
          self.score= float (score)

          print("Student Information:")
    
    # A function to change the name of the student
    def change_name (self, new_name):
          self.name= new_name
          print("name", self.name)

    # A function to change the age of the student
    def change_age(self, new_age):
          self.age = new_age
          print("age", self.age)

    # A function to add track to existing list of tracks
    def add_track(self, added_track):
          self.tracks.append(added_track)
          print("tracks", self.tracks)

    # A function to get the student's score
    def get_score (self):
        return(self.score)

#creating an Instance of the class together with the properties
Bob = Student (name="Bob",age= 26, tracks=["FE","BE"],score= 20.90)

# Expected methods
print(Bob.change_name ("Sia") )
print (Bob.change_age (74) )
print(Bob.add_track("JAVA"))
print(Bob.get_score())





