# * arbitary - unlimited arguments
def call(*args):
    print(args)
call(1,2,3,"four")  # return tuple

# arbitary, keyword arguments
def person(**kwargs):
    print(kwargs)
person(fname = 'Haider', lname = 'chowdhury', agent =25)  #return dictionary

def test(*args, **kwargs):
    print(args,kwargs)

test(1,2,3,"four",fname = 'Haider', lname = 'chowdhury', agent =25)  #return tuple & dictionary