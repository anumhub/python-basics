# List is built-in datatype that stores set of values
# it can store elements of different types

marks=[87,64,33,95,76]
print(marks[0:3]) # ending index is not included  [87, 64, 33]
print(marks[1:4]) # index 4 is not included [64, 33, 95]
print(marks[1:])  #marks[1:len(marsks)]  [64, 33, 95, 76]
print(marks[:3])  # marks[0:3] [87, 64, 33]

#slicing
print(marks[-3:-1])  #sting list from back side    87= index -5, 33= index -3, 76= index -1  [33, 95]
# list methods
lists=[2,1,3]
lists.append(4)
print(lists)  # [2, 1, 3, 4]
lists.sort()
print(lists)  # [1, 2, 3, 4]
lists.sort(reverse =True)
print(lists) # [4, 3, 2, 1]
lists.reverse()
print(lists)  # [1, 2, 3, 4]

listch= ["banana","orange","apple"]
listch.sort()
print(listch) # ['apple', 'banana', 'orange']

listch.insert(1,"peach")  # insert peach on index 1
print(listch) # ['apple', 'peach', 'banana', 'orange']

list1= [1,3,5,7,8]
list1.remove(7)
print(list1) # [1, 3, 5, 8]

list1.pop(2) # pop  value from index 2
print(list1) # [1, 3, 8]


# -----------------------------Tuples ----------------------------------------------

# a built in datatype that lets us create immutable sequences of values
# ( user can't change the values)

tup= (1,2,3,4,5,6)
print(tup)  # (1, 2, 3, 4, 5, 6)
print(tup[0]) #1
print(tup[1])  #2
print(tup[2:5]) # (3, 4, 5)

# create empty tuple
tup1=()
tup2=(1,)
print(tup1) # ()
print(tup2) # (1,)
print(type(tup1)) # <class 'tuple'>
print(type(tup2)) # <class 'tuple'>

tup3=(1)
print(tup3) # 1
print(type(tup3))  # <class 'int'>

# slicing in tuples

tup4=(1,2,3,4)
print(tup4[1:3]) # (2, 3)

tup5=(2,1,3,1)

print(tup5.index(1))  # tup.index(element) returns index of first occurence 1
print(tup5.count(1))  # counts total occurences 2

# WAP to ask the user to enter names of 3 fav movies and store them is list
movies=[]
mov1=input("enter the first movie ")
mov2=input("enter the second movie ")
mov3=input("enter the third movie ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)


# WAP to check if a list contains a palindrome of elements
# for example  racecar,maam, [1,2,3,2,1]
# logic  - make a copy and then reverse it

list11=[1,2,1] #or ["m","a","a","m"]
list122=[1,2,3]
copy_list11= list11.copy()
copy_list11.reverse()

if(copy_list11 == copy_list11):
    print("palindrome")
else:
    print("not palindrome")

#WAP to count the number of students with "A" grade in the following tuple.
#["C","D","A","A","B","B","A"]

grade=("C","D","A","A","B","B","A")
print(grade.count("A")) #3

#store the above values in a list and sort them from "A" to "D"
grade1=["C","D","A","A","B","B","A"]
grade1.sort()
print(grade1) # ['A', 'A', 'A', 'B', 'B', 'C', 'D']





