class Student:
    def __init__(self, height=160):
        self.height = height
nick = Student()
kate = Student(height=170)
sheldon = Student(height=190)
print(nick.height)
print(kate.height)
print(sheldon.height)