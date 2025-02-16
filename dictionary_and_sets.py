#Dictionary are used to store data values in Key:Value pairs
# they are unordered, mutable(changable) and don't allow duplicates keys
from codecs import make_identity_dict

info = {

    "key": "value",
    "name": "anum",
    "learning":"coding",
    "subjects":["python","C","Java"],
    "topics":("dict","set"),
    "age":35,
    "is_adult": True,
    "marks": 98.4,
     12:"integerkey",
     22.33:"floatkey"
}
print(info)
# {'key': 'value', 'name': 'anum', 'laerning': 'coding',
# 'subjects': ['python', 'C', 'Java'],
# 'topics': ('dict', 'set'), 'age': 35, 'is_adult': True, 'marks': 98.4, 12: 'integerkey', 22.33: 'floatkey'}

# accessing the key value

print(info["name"]) #anum
print(info["topics"]) # ('dict', 'set')
print(info["age"]) #35
print(info[12]) #integerkey

# change the name key value
info["name"] ="Anil" # value is overwrite
print(info) # {'key': 'value', 'name': 'Anil', 'learning': 'coding', 'subjects': ['python', 'C', 'Java'],
# 'topics': ('dict', 'set'), 'age': 35, 'is_adult': True, 'marks': 98.4

# add new key:value pair
info["surname"]="Sharma"
print(info) # {'key': 'value', 'name': 'Anil', 'learning': 'coding', 'subjects': ['python', 'C', 'Java'], 'topics': ('dict', 'set'), 'age': 35,
# 'is_adult': True, 'marks': 98.4, 12: 'integerkey', 22.33: 'floatkey', 'surname': 'Sharma'}

# create empty dictionary
null_dict={}
print(null_dict) # {}

#nested dictionary
student={
    "name":"rahul kumar",
    "subjects":{
    "phy":76,
    "chem":88,
    "math":89
    }
}

print(student) # {'name': 'rahul kumar', 'subjects': {'phy': 76, 'chem': 88, 'math': 89}}

print(student["subjects"]) # {'phy': 76, 'chem': 88, 'math': 89}

print(student["subjects"]["phy"]) #76

# dictionary methods
print(student.keys()) # returns all keys------->  dict_keys(['name', 'subjects'])
print(list(student.keys()))  # typecasting into list----------  ['name', 'subjects']
print(student.values()) # returns all values-----> dict_values(['rahul kumar', {'phy': 76, 'chem': 88, 'math': 89}])

print(student.items())  # returns all key values pairs as tuples
# dict_items([('name', 'rahul kumar'), ('subjects', {'phy': 76, 'chem': 88, 'math': 89})])

print(len(student)) # 2

print(student.get("name")) # rahul kumar
print(student["name"]) # rahul kumar

print(student.get("name2")) # None
# print(student["name2"]) # Key Error

student.update({"city":"Delhi"})
print(student) # {'name': 'rahul kumar', 'subjects': {'phy': 76, 'chem': 88, 'math': 89}, 'city': 'Delhi'}

student.update({"name":"Neha Kumari"})
print(student) # {'name': 'Neha Kumari', 'subjects': {'phy': 76, 'chem': 88, 'math': 89}, 'city': 'Delhi'}

# ------------------------------------SET----------------------------------

# set is the collection of unordered items
# each element in the set must be unique and immutable
nums = {1,2,3,4}
set2 ={1,2,2,2} # repeated elements stored only once , so resolved to {1,2}

print(nums) # {1, 2, 3, 4}
print(type(nums))  # <class 'set'>
print(set2) # {1, 2}
print(len(nums)) # 4

null_set=set() # empty set syntax
print(type(null_set))  # <class 'set'>

# set is mutable
# set elements are immutable

# set methods

null_set.add(1)
null_set.add(2)
null_set.add(2)

print(null_set) # {1, 2}
null_set.remove(1)
print(null_set) # {2}

null_set.clear()
print(null_set)

colect= {"hello","mycollge","world","bayarea","QA","python"}

print(colect.pop())
print(colect.pop())
print(colect) # {'mycollge', 'python', 'world', 'hello'}
colect.clear()
print(colect)   # set()

"""
set.union(set2)   combines both set values and return new
set.intersection(set2)   combines common values and return new 
"""

setfirst={1,2,3}
setsecond={3,4,5}

print(setfirst) #{1, 2, 3}
print(setsecond) #{3, 4, 5}
print(setfirst.union(setsecond)) # {1, 2, 3, 4, 5}
print(setfirst.intersection(setsecond)) #{3}

# WAP to store following word meaning in python dictionary :
# table :"a peice of furniture","list of facts & figures"
# cat: "a small animal"

python_dictionary ={
    "cat": "a small animal",
    "table" :["a peice of furniture","list of facts & figures"]
}
print(python_dictionary) # {'cat': 'a small animal', 'table': ['a peice of furniture', 'list of facts & figures']}




# you are given a list of subjects for students. assume 1 classroom is required for 1 subject. how many classrooms are needed by all students
# "python", "java", "C++","python","javascript","java","python","java","C++","C"

subjects={"python", "java", "C++","python","javascript","java","python","java","C++","C"}  # use sets

print(len(subjects))


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one.
# use subject name as key and marks as value

marks= {} # empty dictionary

x=int(input("enter the marks"))

marks.update({"pyh": x})

x=int(input("enter the marks"))

marks.update({"chem": x})

x=int(input("enter the marks"))

marks.update({"math": x})

print(marks)

# figure out a way to store 9 & 9.0 as seperate values in the set

# make 9.0 as string
values={9,"9.0"}
values1={"9",9.0}
print(values) # {9, '9.0'}
print(values1)

# another solution- make a pairs of tuples

values2={
    ("float",9.0),("int",9)
}

print(values2) # {('int', 9), ('float', 9.0)}



