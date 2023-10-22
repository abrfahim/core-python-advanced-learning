

mytuple = (1,2,3,4,5,6,7,8,9)

for i in mytuple:
    print(i)

mylist = [(4, 3, 'arham'),(5,10,15),(5, 'alo', 'arham')]

for i,j,h in mylist:
    print(f"{i} {j} {h}")
print('----------------------------------------------------------------')

mydict = {'name':'Abrar Fahim', 'Age': 25, 'city':'Dhaka'}
for key,value in mydict.items():
    print(f"key: {key} , value:{value}")
