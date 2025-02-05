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
print(firstname)
print(len(firstname))

# write a program to find the occurence of '$' ina  string
word_occurance= "Hi, $Iam the $ symbol $10.00"
print(word_occurance.count("$"))

