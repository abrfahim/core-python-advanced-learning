"""
A function is called Higher Order Function if it contains other functions as a parameter or
 returns a function as an output i.e, the functions that operate with another function are
  known as Higher order Functions.
"""

def hof(fn):
    print(fn.__name__)
    fn()

def greeting():
    print("Hello, welcome to the world of hope")

def x():
    print("Hello,You are not str")

hof(x)

