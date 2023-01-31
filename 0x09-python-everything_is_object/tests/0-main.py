#type() Syntax

#The type() function has two different forms:

# type with single parameter
#type(object)

# type with 3 parameters
#type(name, bases, dict)



#Example 1: type() with Object parameter
prime_numbers = [2, 3, 5, 7]

# check type of prime_numbers
result = type(prime_numbers)
print(result)


#Example 2: type() With 3 Parameters
o1 = type('X', (object,), dict(a='Foo', b=12))
print(type(o1))

print(vars(o1))

class test:
  a = 'Foo'
  b = 12
  
o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))
print(vars(o2))