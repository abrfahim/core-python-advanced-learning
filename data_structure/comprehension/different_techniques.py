
mylist = [1,2,3,4,5,6,7,8,9]
mynewlist = [i+1 for i in mylist]
print(mynewlist)

# list conversion
myDict = {i: i*i for i in mylist}
print(myDict)

mySet = {i*i*i for i in mylist}
print(mySet)

myTuple = tuple(i**4 for i in mylist)
print(myTuple)

myTupleList = [(i,i**2)for i in mylist]
print(myTupleList)

print('----------------------------------------------------------------')

# Dictionary Conversion

dict = {'Name':'Warn Gets', 'Age':30, 'city':'New York',}
toListK = [k for k,v in dict.items()]
print("keys:",toListK)
toListV = [v for k,v in dict.items()]
print("values:",toListV)
