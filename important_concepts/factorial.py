"""
To find the Python factorial of a number, the number is multiplied with all the integers
 that lie between 1 and the number itself. Mathematically, it is represented by “!”.
 Thus, for example, 5! will be 5 x 4 x 3 x 2 x 1, that is 120. Factorial for negative
 numbers is not defined.
"""

def factorial(n):
    if n == 1:
        return 1
    m = factorial(n-1)
    return  n*m

print(factorial(5))

