
class Person:

     # instance attributes - different for different objects
     # self - indicate own properties or attributes
    def __init__(self,name,age,university,subject):
        self.name = name
        self.age = age
        self.university = university
        self.subject = subject

    # instance methods - different for different objects
    def introduction(self):
        print("My name is {}, I'm {}.I have a bachelor degree from {} on {}."\
            .format(self.name, self.age, self.university, self.subject))

Man1 = Person('Abrar Fahim', 25, 'PortCity University', "EEE")

Man1.introduction()