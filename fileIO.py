# python can be used to perform operations on a file ( read and write data)
"""
test files = .txt, .docx, .log etc
binary files = .mp4, .mov, .png, .jpeg etc

chaaracters:
r= open the file for reading
w= open  for writing, tructating the first file
x= create a new file and open it for writing
a= open for writing, appending to end of file if it exists
b= binary mode
t= text mode (default mode)
+= open a disk file for updating
"""
from syslog import openlog

# opening the file and closing the file
f=open("demo.txt", "r")
data=f.read() # reads entire line
print(data)
print(type(data))
f.close()

# if we want to read first 5 characters
f=open("demo.txt", "r")
data=f.read(5)
print(data)
f.close()

# if we want to read line by line
f=open("demo.txt", "r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()

# write the file
f=open("demo.txt","w")
f.write("Hi Good Morning whatup... i am learning pyton looks interested to me ")
f.close()

# open the file and see if new changes are reflected . it will overwrite all previous content
f=open("demo.txt", "r")
data=f.read(5)
print(data)
f.close()

# append the data in file . it will add new data at the end
f=open("demo.txt", "a")
f.write("\nyou can also learn with me")
f.close()

# open the file and see if new changes are reflected
f=open("demo.txt", "r")
data=f.read()
print(data)
f.close()

"""
the argument mode points to a string beginning:
r = open text for reading. the stream(pointer) is positioned at the beginning of the file
r+= open the reading and writing. the stream is positioned at the beginning of the file.
w= truncate file to zero length or  create text file for writing. the stream is positioned at the beginning of the file
w+= open for reading and writing.
a= open for writing. the stream is positioned at the end of the file
"""

# demo1.txt = this is a sample document.
f=open("demo1.txt", "r+")
f.write("abc")
print(f.read()) # s is a sample document.
f.close()

with open("demo.txt", "r") as f:
     data=f.read()
     print(data)

with open("demo.txt", "w") as f:
    f.write("new data")


# deleting a file - using the of module
# module ( like a code library) is a file written by another programmer that generally has a functions we can use

import os
#os.remove("sample.txt")


# create a new file "practice.txt using python. Add the following data in it:
"""
Hi everyone
we are learning file I/O
using Java.
i like programming in Java
"""
with open("practice.txt","w") as f:
    f.write("Hi everyone\n we are learning file I/O\n using Java.\n i like programming in Java")

# WAF that replace all the occurances of java with python in above file
with open("practice.txt","r") as f:
    data=f.read()
new_data= data.replace("Java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

# search if the word "learning" exists in the file or not

def check_for_word():
    with open("practice.txt", "r") as f:
        word = "learning"
        data = f.read()
        if (data.find(word)!= -1):
            print("found")
        else:
            print("not found")

check_for_word()

#WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found

def check_for_line():
    word1="learning"
    data1=True
    line_no=1
    with open("practice.txt", "r") as f:
        while data1:
            data1 = f.readline()
            if(word1 in data1):
                print(line_no)
                return
            line_no+=1

    return -1

check_for_line()



# from a file containing numbers seperated by comma, print the count of even numbers

with open("practice1.txt","w") as f:
    f.write("1,4,76,88,101,90")

count=0
with open("practice1.txt", "r") as f:
    data=f.read()
    nums=data.split(",")
    for val in nums:
        if(int(val)%2 ==0):
            count+=1

print(count)



