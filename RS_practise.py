str="Hello World"
print(str)

b=5
c=6.4
d="Great"

print("value is",b)
print(type(b))

print("{} {}".format("Value is",b))

# lists

values=[1,2,"abc",4,5]

print(values[0])
print(values[3])
print(values[-1]) #5
print(values[1:3]) # 2 , abc
values.insert(3,"def")
print(values)
values.append("end")
print(values)

values[2] = "wow"  # update

del values[0]
print(values)
