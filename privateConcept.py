"""
private attributes and metgods are meant to be used within the class and are not accessible from outside the class
"""


class Person:
    __name="anonymous"  # private attibute

    def __hello(self):  # private method
        print("Hello person")

    def welcome(self):
           self.__hello()


p1 = Person()

#print(p1.__hello()) # this is throw error

print(p1.welcome())