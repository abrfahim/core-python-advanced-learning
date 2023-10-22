"""
A decorator is a design pattern in Python that allows a user to add new functionality to an
existing object without modifying its structure.

# way 1 - wrapper function

Wrappers around the functions are also knows as decorators which are a very powerful and
useful tool in Python since it allows programmers to modify the behavior of function or class.
"""

def immut():
    print("Don't touch me")

def mut(immut):
    immut()
    print("I don't touch you, but you will be changed")
mut(immut)

print('----------------------------------------------------------------')


@mut
def mix():
    print("wait to see, what can I do'")
