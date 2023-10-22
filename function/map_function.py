
def func(n):
    return n**3

li = [1,2,3,4,5,6,7,8,9]

newList = list(map(func,li))
newSet = set(map(func,li))
newTuple = tuple(map(func,li))
print(newSet)
print(newList)
print(newTuple)