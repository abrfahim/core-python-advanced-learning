# return a list of squres of given items

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
newlist = []

for i in mylist:
    newlist.append(i*i)
print(newlist)

print('--------------------------------')

#using comprehension techniques => store, loop, condition

compList = [i*i for i in mylist]
print(compList)


print('--------------------------------')
quebeList = [i*i*i for i in mylist]
print(quebeList)

print('--------------------------------')
evenList = [i*i for i in mylist if i%2==1]
oddList = [i*i for i in mylist if i%2==0]
print(evenList)
print(oddList)