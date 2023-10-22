"""
Python also accepts function recursion, which means a defined function can call itself
"""

# def recur(n):
#     print(n)
#     recur(n+5)        # recur function called it self
# recur(10)

# print 1 to 20 using recursion fucntion

def counting(n):
    if n>20:
        return
    print(n)
    counting(n+1)
counting(1)