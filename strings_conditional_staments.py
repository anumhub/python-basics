# string is datatypes stores sequence of characters
from operator import length_hint

str1="this is a string.we are creating it in python."
str2="this is a string.\n we are creating it in python."
str3="this is a string.\t we are creating it in python."

print(str1)
print(str2)
print(str3)

str4="good"
str5="morning"
final= str4 + " " +str5
print(final)  # good morning
print(len(final))  # 12

# indexing- help in only  to access characters, we can't change the characters values

str6= "my college"
ch= str6[0]
print(ch) # m

# slicing - accessing parts of a string

str7= "managementdecision"
print(str7[1:4])  # ana  will print from index 1 to 3 , not 4
print(str7[5:9])  # emen
print(str7[:9])  # managemen #[0:8]
print(str7[8:])  #ntdecision  # [ 5:len(str)]

#negative index

str8="Apple"  # A= -5, p=-4, p=-3, l=-2,e=-1
print(str8[-3:-1]) #pl  -1 index is not included


#string functions
stringf= "i am a coder"
print(stringf.endswith("er"))  # true
print(stringf.endswith("am"))  # false

print(stringf.capitalize())  # I am a coder
print(stringf.replace("coder","tester")) # i am a tester
print(stringf.find("a")) # result is the index position 2
print(stringf.find("b"))   # -1   there is no negative index, so -1 is invalid index
print(stringf.count("a"))  # 2

# write a program to input user first name and print its length

firstname= input(("enter the firstname: "))
print(firstname)  # sam
print(len(firstname))  #3

# write a program to find the occurence of '$' ina  string
word_occurance= "Hi, $Iam the $ symbol $10.00"
print(word_occurance.count("$")) # 3

#--------------------------Conditional Statements -----------------
"""
syntax
if-elif-else
"""

# if statement example
age =21
if age > 18:
    print("can't vote")

# elif and else statement example

light=("blue")
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")
print("end of the code")

# another example

marks=74
# marks= int(input("enter the marks:"))
if(marks >= 90):
    grade ="A"
elif(marks >= 80 and marks < 90):
    grade="B"
elif(marks >= 70 and marks < 80):
    grade="C"
else:
    grade= "D"
print("grade of the student ->",grade)

#nesting - statements in another statment
age =34
if(age  >= 18):
    if(age >=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("can't drive ")


#WAP to check number is even or odd

num=14
rem=num%2
if(rem == 0):
    print("number is even")
else:
    print("number id odd")

#WAP to check number is multiple of 7

num=14
rem=num%7
if(rem == 0):
    print("number is multiple of 7")
else:
    print("number ids not multiple of 7 ")

# WAP to find greastest of 3 numbers entered by user

a=4
b=5
c=7
if(a>b and a>c):
    print("first number is greatest")
elif(b>c):
    print("second is grestest")
else:
    print("third is greatest")