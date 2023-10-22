# Python has the following data types built-in by default, in these categories:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, byte array, memory view
# None Type:	NoneType
#Casting, also known as type conversion, is a process that converts a variable's data type into another data type.
# These conversions can be implicit (automatically interpreted) or explicit (using built-in functions).

value = float('150.5')  #convert to float
print(value)
print("the type is:", type(value))

number = int("10")  #convert to int
print(number)
print("the type is:", type(number))

value2 = str(value) #convert to string
print(value2)
print("the type is:", type(value2))