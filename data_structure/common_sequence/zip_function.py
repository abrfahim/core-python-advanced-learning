mylist =['apple', 'banana','candy','cheese','burger','lemons','sandwich']
mylist2 =['biriyani', 'teheri','chips','jhalmuri']
mylist3 = list(range(len(mylist)))
print(mylist3)

print('--------------------------------')

for i in zip(mylist,mylist2):
    print(i)

print('--------------------------------')

for i,j in zip(mylist3,mylist):
    print(i,j)