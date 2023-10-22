"""
Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute.
 Python supports classes inheriting from other classes. The class being inherited is called the Parent
  or Superclass, while the class that inherits is called the Child or Subclass.
"""
class A:
    def __init__(self,name):
        self.name = name
        print("I am from A")

    def hello(self):
        print("I am from hello function")

class B:
    def __init__(self,age):
        self.age = age
        print("I am from B")

    def hi(self):
        print("I am from hi function")

class C(A,B):
    def __init__(self):
        pass

obj = C()
obj.hi()
print(C.__mro__)
