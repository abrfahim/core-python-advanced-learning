# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#
# Operator	                                            Description	                            Example
# is 	                                Returns true if both variables are the same object	    x is y
# is not	                        Returns true if both variables are not the same object	    x is not y

# if memory location is different then object is not the same
x=5
y=5
a = []
b= []
# id allocates memory location
print(id(x))
print(id(y))
print(x is y)
print(x is not y)

print(id(a))
print(id(b))
print(a is b)
print(a is not b)