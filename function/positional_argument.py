
def fullName(fname,lname):
    print("Hello, Mr. {} {}".format(fname,lname))

fullName('Abrar', 'Fahim')

print('----------------')

# Resturant tax
def resTax(pay,tax=5):
    total = pay + pay*(tax/100)
    print("Your net bill: ",total)
resTax(500)

def sum(a,b):
    print(a+b)
sum(7,8)

def substract(a,b):
    print(a-b)
substract(25,7)

print('----------------')

a = int(input('Enter Your value:'))
b = int(input('Enter Your value:'))
def eo(a,b):
    if (a%2==0):
        print(a,'is even')
    else: print(a, 'is odd')
    if (b%2==0):
        print(b,'is even')
    else: print(b,'is odd')

eo(a,b)