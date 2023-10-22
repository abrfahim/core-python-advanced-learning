"""
class Meta is basically the inner class
"""
myString ="Sonet Chowdhury"
myNum = 36
myDict = {'Nmae':'Abrar Fahim', 'Age': 25}
myList = [1,2,3,4,5]

print(type(myString))
print(type(myNum))
print(type(myDict))
print(type(myList))

# so everything is an object of class

# type is a meta class for test class
class test:
    def __init__(self,name):
        self.name = name
        print("hello world")

obj = test("who")

print(type(test))
print(type(obj))