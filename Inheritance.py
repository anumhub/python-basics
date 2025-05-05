""""
when 1 class(child/derived) derives the properties and methods of another class(parent/base)

single heritance
multi -level inhertitance
multiple inheritance
"""

class Car:
    coloe = "Black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1 = Fortuner("diesel")
car1.start()


# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")
# print(car1.name)
# print(car2.start())  # inheritance property used


"""
multiple inheritance 
class A:
  varA = "welcome to class A"
  
class B:
varB="welcome to class B"

class C(A,B):
 varC="welcome to class C"
 
c1 =C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


------------------------------

super() method is used to access methods of the parent class


class Car:
    def __init__(self, type):
        self.type=type
        
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        
car1 = ToyotaCar("prius,"electric")
print(car1.type)
"""