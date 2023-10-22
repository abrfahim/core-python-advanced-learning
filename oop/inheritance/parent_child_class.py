'''
Inheritance allows us to define a class that inherits all the methods and properties from
another class. Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''

#parent class
class Person:
    def __init__(self,name,city):
        self.name = name
        self.city = city
    def intro(self):
        print ("Hey, this is {} from {}".format(self.name, self.city))

# child class
class Student(Person):
    def __init__(self,name,city,skills):
        self.skills = skills
        Person.__init__(self, name, city)

student1 = Student('Ahemd Nazmul','Chittagong',["python","java"])

student1.intro()