"""
Immutable objects are quicker to access and are expensive to change because it involves the creation
 of a copy. Whereas mutable objects are easy to change. The use of mutable objects is recommended
 when there is a need to change the size or content of the object.
"""

name = "My name"
print(type(name))
print(id(name))

# a = 'Hello, world'
# print(a[0])
# a[0] = 'k'          #not possible to change; its immutable
# print(a[0])

b =['Hello', 'world', 'Hi', 'sigma']
print(b[0])
b[0] = 'Rounding'
print(b[0])             # possible to change this; mutable

print('----------------------------------------------------------------')

c = (1,2,3,4,5,6,7,8,9) #tupple immutable

d = (1,[8,9,0],3,4,5,)  # this tuple including a list; so we can just change the list not the tuple
d[1][1] = 15

print(d)