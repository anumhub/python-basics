# class is a blueprint for creating objects

# creating class
class student:
    name = "killy kiran"
    def __init__(self): # initilizing constructor
        print(self) # <__main__.student object at 0x108b0fcb0>
        print("adding new student in database")

# constructor
"""
all classes have a function called __init__(), which is always executed when the object is being initiated
the self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class

class student:
    def __init__(self, fullname,marks):
         self.name=fullname  ( instance  attribute)
         self.marks=marks
         
s1=Student("killy",93)
print(s1.name,s1.marks)
"""

# creating objects(instance)
s1=student() # parenthesis is used to call constructor
print(s1.name)

class CollegeStudent:
    college_name="ABC college"  # class attribute
    name="anonymous" #class attribute

    @staticmethod
    def college(): # static method that donot use self parameter
        print("ABC college")

    def __init__(self, name, marks):
        self.name = name # obj attr > class attr
        self.marks = marks
    def welcome(self):
        print("welcome student ",self.name)

    def get_marks(self):
        return self.marks

stu1 = CollegeStudent("Mona", 98)
print(stu1.name, stu1.marks)
stu2 = CollegeStudent("Helen", 77)
print(stu2.name, stu1.marks)
print(stu2.college_name)
stu1.welcome()
print(stu1.get_marks())  # return the value - marks
# methods
# methods are functions that belong to objects


# Absctraction- hiding the implementaion details of a class and only showing essential features
# to the user
# Encapsulation - wrapping data and functions into a single unit(object)

class Car:
        def __init__(self):
            self.accelarator=False
            self.brk=False
            self.clutch=False
        def start(self):
            self.clutch=True
            self.accelarator=True
            print("car started")
car1=Car()
car1.start()





"""
class attribute - when value is stored 1 time ( common in objects for example - college name = ABC
object or instance attribute - stroing value for different objects ( student 1, student 2)

object attribute preference is more than class attribute 

"""