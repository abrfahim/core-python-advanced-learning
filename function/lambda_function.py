# Lambda functions are similar to user-defined functions but without a name.
# They're commonly referred to as anonymous functions.

# Regular functions converting to lambda functions
def sum(a, b):
    print(a + b)

# step=>    store the function; lambda keyword ; argument ; expressions

lambda_sum = lambda a,b : print(a,'+', b, '=',a + b)
lambda_sum(3,4)
print('--------------------------------')

def sub(a,b):
    print(a - b)

lambda_sub = lambda a,b : print(a,'-', b, '=',a - b)
lambda_sub(20,10)
print('--------------------------------')

def avg(x,y):
    print(x+y/2)

lambda_avg = lambda a,b: print(a,'+', b,'/','=',(a + b)/2)
lambda_avg(20,10)

print('--------------------------------')

def check_even_odd(a,b):
    if (a%2==0):
        print(a,'is even')
    else: print(a, 'is odd')
    if (b%2==0):
        print(b,'is even')
    else: print(b,'is odd')

lambda_eo = lambda x,y : print(x,'is even' if x%2==0 else 'is odd') or print(y,'is even' if y%2==0 else 'is odd')

lambda_eo(7,4)