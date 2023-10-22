# In Python, dictionaries are mutable data structures that allow you to store key-value pairs.
# Dictionary can be created using the dict() constructor or curly braces' {}'.

person ={
    'name': 'Abrar',
    'Age': 25,
    "Location":"Dhaka"
}
# name, age, location are key
print(person)

sell ={
    'courses': ['python', 'javascript','java'],
    "tuitionFees" : [5000, 5000, 5000]
}
print(type(sell))
print(sell)

# empty dictionary
empty = {}
nulld = dict()
print(type(empty))
print(type(nulld))