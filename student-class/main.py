class Student:
    """Student Class"""
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
    
    def change_name(self, new_name):
        self.name = new_name
        return self.name
        
    def change_age(self, new_age):
        self.age = int(new_age)
        return self.age

    def add_track(self, new_track):
        self.tracks = self.tracks+[new_track]
        return self.tracks

    def get_score(self):
        return self.score

# Defining an object
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# applying the methods to the object of the class.
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())
print("\n")
# print new details of Bob
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)