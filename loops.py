# loop are used to repeat instructions

"""
while Loops
    while condition:
    # some work
    # some updation
"""

i=1 # i is iterator
while i<=5 :
    print("Hello",i)
    i = i + 1

print("loop ended")

y=5
while y>=1: # stopping condition
    print(y)
    y=y-1
print("loop ended")

# print numbers from 1 to 100
j=1 # i is iterator
while j<=100 :
    print("Hello",j)
    j = j + 1

print("loop ended")
# print numbers from 100 to 1
x=100
while x>=1: # stopping condition
    print(x)
    x=x-1
print("loop ended")
# print the multiplication table of number n
n=4
j1=1
while j1<=10 :
    print(n*j1)
    j1+= 1
print("loop ended")
# print the elements of the following list using loops:
#[1,4,9,16,25,36,49,64,81,100]

e1=[1,4,9,16,25,36,49,64,81,100]
# traverse the list items
totale1= (len(e1))
idx=0
while idx<len(e1):
    print(e1[idx])
    idx+=1

print("loop ended")
# search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)

search_number_list= (1,4,9,16,25,36,49,64,81,100,36)
search_number=36
k=0
while k<len(search_number_list):
    if(search_number_list[k] == search_number):
        print("found at index",k)
    else:
        print("finding.....")
    k+=1
print("loop ended")

# break - used to terminate the loop when encountered

search_number_list= (1,4,9,16,25,36,49,64,81,100,36)
search_number=36
k=0
while k<len(search_number_list):
    if(search_number_list[k] == search_number):
        print("found at index",k)
        break
    else:
        print("finding.....")
    k+=1
print("loop ended")
# continue - terminates excution in the current iteration & continues execution of the loop with the next iteration

v1=0
while v1<=5:
    if(v1==3):
        v1+=1
        continue # skip  below 2 lines
    print(v1)
    v1+=1

#program to check number is odd
v2=1
while v2<=10:
    if(v2%2 == 0):
        v2+=1
        continue # skip  below 2 lines
    print(v2)
    v2+=2

    v3 = 1
    while v3 <= 10:
        if (v3 % 2 != 0):
            v3+= 1
            continue  # skip  below 2 lines
        print(v3)
        v3+= 1

# loops are used for sequwntial traversal. For traversing list, string, tuples
"""
for Loops
for el in list:
  # some work 
  
for el in list:
  #some work
else:
 # work when loop ends
"""
#list
veggies=["potato","brijal","landfinger","cucumber"]
for val in veggies:
    print(val)
#tuples
tup=(1,2,3,4,5,6,7)
for num in tup:
    print(num)

#string
str="helloeveryone"
for char in str:
    print(char)

str1="goodmorning"
for char in str1:
    if(char == "r"):
        print("r found")
        break
    print(char)
else:
    print("END")

# using for
# print the elements of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]

element= [1,4,9,16,25,36,49,64,81,100,49]
x1=49
idx1=0
for el in element:
    if(el == x1):
        print("number found at index",idx1)
        break
    idx1+=1

#range()
# returns of sequence of numbers, starting from 0 by default and inctements by 1 and stops by a speciied number
# range(start?,stop,step?)
print("range example :-" )
print(range(5)) # range(0, 5)
seq=range(10) #range(stop)
for i in seq:
    print(i)

print("range example :-" )
for l in range(2,10): # range(start,stop)
    print(l)

print("range example :-" )
for ss in range(2,14,2): # range(start,stop,step)
    print(ss)


# search  for a number x in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)

tup1=(1,4,9,16,25,36,49,64,81,100)

# print numbers from 1 to 100
for dd in range(1,101):
    print(dd)
# print numbers from 100 to 1
for det in range(100,0,-1):
    print(det)
# print the multiplication table of a number n
n=int(input("enter the number "))
for ne in range(1,11):
    print(n*ne)

#pass statement
# pass statement is a null statement that does nothing. it is used as a placeholder for future code.
"""
for el in range(10):
    pass
"""
for kk in range(5):
    pass
if i>9:
    pass
print("some useful work`")


# WAP to find the sum of first n numbers ( using while)
num1=5
sum=0
l=1
while(l <=n):
    sum+=l
    l+=1
for i in range(1,num1+1):
     sum+=num1
print(("total sum is ",sum))


#WAP to find the fractional of first n numbers (using for)

fac=1
for i in range(1,num1+1):
     fac*=num1
print("factiorail is ",fac)
