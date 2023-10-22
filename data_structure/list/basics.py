# Lists is a collection of items
# used to store multiple items in a single variable.
# list items are ordered, changeable, and allowed duplicate values.
# square braaces indicates list

mylist = ["apple", "banana", "cherry"]
#  length     1          2        3
# index       0         1         2
#negative     -3        -2       -1
dummyList = ["apple", "banana", "cherry", 1, 2, 1, 1.5, 2.7, 12.5, {1,2,3,4,5,6,7},['a', 'b']]

print(dummyList)

# indexing starts from 0 and negative indexing starts from -1(last element)
print(mylist[0])
print(mylist[-1])
print(len(mylist))

#update value of list
mylist[0] = "Mango"
print(mylist[0])

# list methods:
# Remove list element  using del method
del mylist[1]
print(mylist)

# Remove list element  using pop method
rmv = dummyList.pop() #remove last element from list
print(dummyList)
print("removed item was:",rmv) #return poped item

# Remove specific list element using pop method
remv =dummyList.pop(1)
print("removed item was:",remv)
print(dummyList)

# remove method
vowel = ['a','e','i','o','u','d']
vowel.remove('d')
print("vowel",vowel)

num =[0,1,2,3,4,5,6,7,8,9,10]
# slicing    [start:end:step]           start=0; end= -1; step= 1(default)

print('slicing part:',num[2:6])
print('slicing part:',num[2:-1])
print('slicing part:',num[0:-1])
print('slicing part:',num[2:])

#step
print('even part:', num[0::2])
print('odd part:', num[1::2])
print('slice part:', num[0:-1:3])

#reverse list using slice
print('reverse list:',num[-1:-12:-1])        # -1= last element; len(num) + 1 = 12; step =-1
print('reverse list easy way:',num[-1::-1])