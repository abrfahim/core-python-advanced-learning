class Person:
    # class attributes - same for all objects
    skills = "Java, Python, Django"

    # class methods - same for all objects
    # cls - indicates class properties
    @classmethod  # decleration
    def skills_name(cls):
        return cls.skills_name()

    # instance attributes - different for different objects
    def __init__(self,name):
        self.name = name

    # instance methods
    def introduction(self):
        print("Hello, I am {}".format(self.name))


Man1 = Person('Sonet Ahmed')
Man1.introduction()
print(Person.skills)
print(Man1.skills)
