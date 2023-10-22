employee ={
    'name':'Abrar Fahim',
    'skills':['python', 'javascript', 'django'],
    'experience': 4,
}

# key,value methods
print(employee.keys())
print(employee.values())

print('________________________________________________________________')
# items methods => return key,value pairs as a list
print(employee.items())
print('________________________________________________________________')

# forloop
for i in employee.keys():
    print(i,":::", employee[i])

print('________________________________________________________________')

# smart way
for key,value in employee.items():
    print(key,"=",value)