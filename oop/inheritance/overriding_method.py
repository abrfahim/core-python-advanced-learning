"""
Method overriding is a feature of object-oriented programming languages where the subclass
or child class can provide the program with specific characteristics or a specific implementation
process of data provided that are already defined in the parent class or superclass.
"""
class User:
    def __init__(self,name, pay):
        self.name = name
        self.pay = pay

    def shipping_cost(self):
        if self.pay > 2000:
            return 50
        return 70

class PremiumUser(User):

    def discount(self):
        if self.pay >3000:
            return 100
        return 50

    def shipping_cost(self):
        return 0


person1 = PremiumUser('Abrar Fahim', 5000)
person2 = User('Sonet Chowdhury', 1200)

print(person1.shipping_cost())
print(person2.shipping_cost())