
total = list(range(1,26))
print(total)

# odd
def func(n):
    return n%2!=0

odd = list(filter(func,total))
print(odd)