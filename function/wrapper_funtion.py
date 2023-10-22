"""
a wrapper is a piece of code that is used to modify or extend the behavior of an existing
 function, method, or class without modifying its source code.
"""

def wrapper(fn):
    def test():
        print('I am from test! before')
        fn()
        print('I am from test! later')
    return test

@wrapper
def hi():
    print('I am from hi')

call = wrapper(hi)
# call()

hi()