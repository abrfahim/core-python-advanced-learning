
employee ={
    'name':'Abrar Fahim',
    'skills':['python', 'javascript', 'django'],
    'experience': 4,
}
print(employee['name'])
print(employee['experience'])

#get method
print(employee.get('skills'))

# change
employee['name'] = 'Sonet Chowdhury'
print(employee['name'])
print('----------------------------------------------------------------')

# update & add multiple items
employee.update({
    'name':'Sajjad Islam',
    'skills':['python', 'javascript', 'React'],
    'experience': 2,
    'salary': 50000             #added new key-value pairs
})
print("After Update:",employee)
print('----------------------------------------------------------------')
# add
employee['focus'] = 'Problem Solving'
print("After adding:",employee)

print('----------------------------------------------------------------')

# remove using del
del employee['salary']
print("After removing:",employee)
print('----------------------------------------------------------------')

# remove using pop
employee.pop('skills')
print("After pop:",employee)

print('----------------------------------------------------------------')

#copy
a = {'vowel':['a','e','i','o','u']}
b = a
print('b:',b)
c = b.copy()
print('c=',c)