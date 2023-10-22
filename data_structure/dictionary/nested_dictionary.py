
courses ={
    1:{
        'name': 'python',
        'fee': 3000
    },
    2:{
        'name': 'java',
        'fee': 5000
    },
    'a':{
        'name': 'django',
        'fee': 3000
    },
    'b':{
            'name':"spring boot",
            'fee': 6000
    }
}

print(courses)
print(courses.keys())
print(courses.values())
print('--------------------------------')

for i,j in courses.items():
    print(i,'=',j)

print('--------------------------------')

# access course 2 fees
print(courses[2]['fee'])

# access course 1 details
print(courses[1])