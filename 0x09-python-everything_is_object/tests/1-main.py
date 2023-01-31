#
# Definition and Usage
#The id() function returns a unique id for the specified object.
#All objects in Python has its own unique id.
#The id is assigned to the object when it is created.

#example
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)