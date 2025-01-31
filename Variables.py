# comments
# hash is used for comments for single line
"""
this is multiline comment
"""


# how to print in python
print("Hello Anum")

# how to store values in varaibles
# examples
My_Name="Anum" # string datatype
age_2028=12 #integer datatype
price22=24.99 # float datatype
old= False # boolean datatype
a=None # null datatype


# print the values

print("my name is: ",My_Name)
print("my age is: ",age_2028)
print("my price is: ",price22)
print(old)
print(a)

# to know the datatype of varaibles

print(type(My_Name))
print(type(age_2028))
print(type(price22))

# expression execution
# string and numeric values can operate together with *
A,B=2,3
Txt="@"
print(2*Txt*3)

# string and string can operate with +
C,D="2",4
Txt2="@"
print((C+Txt2)*D)

#result of division operator with 2 integers will be float
#result of integer division with float and int give displayed as float
var1= 1
var2=2
var4=1.5
var5=3
var6=(var4//var5)
var3=var1/var2
print (var3) #  0.5
print(var6) # 0.0

# reminder is negative if denominator is negative

num1= 5
num2= 2
num3= -2
num4 = num1 % num2  # 1
num5= num1%num3    # -1
print (num4)
print (num5)

first= 4
second =2

# arithematic operators
print( first + second)
print( first - second)
print( first * second)
print( first % second)
print( first / second)
print (first ** second)  #first^ second

# relational operators
print( first == second)
print( first != second)
print( first >= second)
print( first <= second)
print( first > second)
print( first < second)

# assignment operators
a1= 10
a1 **= 5
print("a1 :" , a1) # 100000

# #logical operators
a2=4
a5=7
print(not True) # False
print(not False)  # True

print(not (a2> a5))  # True

val1= True
val2 = False
print(" AND operator value is : ", val1 and val2)  #false
print(" OR operator value is : ", val1 or val2)  #true

# input in python
#taking input from user and print it
yourname= input("name :")
agee=input("age:")
hobby=input("hobby: ")

print("Hi, My name is : ",yourname, "I am ",agee, "years old", "My hobby is", hobby)

