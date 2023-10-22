
from functools import reduce

li = [1,2,3,4,5,6,7,8,9,10]

def func(x,y):
    return x + y

sum = reduce(func,li)
print(sum)