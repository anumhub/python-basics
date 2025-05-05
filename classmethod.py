"""
class method is bound to the class and relatives the class as an implicit first argument

statuc metgod can't access or modify class state and generally for utility

@classmethod
def ChangeName(cls,name):
   cls.name = name

"""

class Person:
    name="anonymous"

    def changeName(self,name):
        #self.name = name
        self.__class__.name = "Harry"

p1= Person()
p1.changeName("Harry")
print(p1.name)
print(Person.name)


"""
types of methods :

static methods - no self ( no access of instance and class)
class methods - (cls, )-  access class attributes 
instance methods - (self,  )  
"""