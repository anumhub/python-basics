
"""
create student class that takes name and marks of 3 subjects as arguments in contructor. then create a method to print
the average
"""
class Student:  # student class
    def __init__(self,name,marks):  # constructor
        self.name=name
        self.marks=marks
    @staticmethod  # static methods works at class level . methods don;t use self parameter
    def college():
        print("Appejay College")

    def get_avg(self): # methos in class , there is always 1 parameter= self
        sum=0
        for val in self.marks:
            sum += val
        print("Hello",self.name,"your average marks is: ",sum/3)


s1=Student("Kelen",[77,89,93])
s1.get_avg()



"""
static methods are decorator allow us to wrap another function in order
to extend the behaviour of the wrapped function, without permanently modifying it

"""