# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# don't allow duplicate elements
# declareed by seconde braces {}

fruits = {"mango","apple","orange","banana","blackberry"}

# check class
print(type(fruits))

#another way to declare set

busket = set(["mango","apple","orange","banana","blackberry"])
print(type(busket))
print(busket)

# empty set declaration
a = set()
print(type(a))

# check items> return a boolean value
print("blackberry" in busket)
print("Blackberry" in busket)