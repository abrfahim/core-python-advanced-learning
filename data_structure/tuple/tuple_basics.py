# Python tuples are a type of data structure that is very similar to lists.
# The main difference between the two is that tuples are immutable,
# meaning they cannot be changed once they are created.
# This makes them ideal for storing data that should not be modified, such as database records.
# declared by () first braces

car = ("audi", "bmw", "ford", "toyota")
print(car)

dummy = ("banana", "apple", "orange", 1,23,34,3,['man', 'woman'])
print(type(dummy))  # check class type
print(dummy)

name = ("abrar")
print(type(name))   #this is not tuple, class str
# more than one element need to be tuple or use a comma

tp = ("abrar",)
print("tp:",type(tp)) #

name2 = ("sonet", "akram")
print(type(name2))  # this is tuple
print("----------------------------------------------------------------")

# accessing tuple
sports = ("football", "cricket", "badminton", "hockey", "hadudu")
print(sports[0])
print(sports[1])
print(sports[-1])
print(sports[-2])