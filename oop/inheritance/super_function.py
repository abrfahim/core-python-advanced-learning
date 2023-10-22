"""
Definition and Usage. The super() function is used to give access to methods and properties of
a parent or sibling class. The super() function returns an object that represents the parent class.
----------------------------------------------------------------
Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy
of classes. Especially it plays vital role in the context of multiple inheritance as single
method may be found in multiple super classes.
"""

# A -> B -> C = Multilevel_Inheritance
class A:
    def __init__(self):
        print('I am Grand-Father: A class')

class B(A):
    def __init__(self):
        print('I am Father: B class')
        super().__init__()

class C(B,A):
    def __init__(self):
        print('I am Son: C class')
        super().__init__()
obj_C = C()
print(obj_C)

print('--------------------------------')

# D = Multiple_Inheritance

class D(C,B):
    def __init__(self):
        print('I can connect to everyone: D class')
        super().__init__()

obj_D = D()
print(obj_D)