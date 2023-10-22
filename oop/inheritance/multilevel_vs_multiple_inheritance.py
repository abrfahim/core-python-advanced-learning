# A -> B -> C = Multilevel_Inheritance
class A:
    def __init__(self):
        print('I am Grand-Father: A class')

class B(A):
    def __init__(self):
        A.__init__(self)
        print('I am Father: B class')

class C(B):
    def __init__(self):
        B.__init__(self)
        print('I am Son: C class')

obj_C = C()
print(obj_C)

print('--------------------------------')

# D = Multiple_Inheritance

class D:
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        C.__init__(self)
        print('I can connect to everyone: D class')

obj_D = D()
print(obj_D)