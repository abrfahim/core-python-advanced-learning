
tp = ('http', 'json', 'javascript', 'xml', 'python')
ls = ['html','css','bootstrp','sass',10]
my_range = range(0,21)

print(my_range)

"""
 common action on sequences:
 ----------------------------------------------------------------
 in - return boolean
 not in - return boolean
 index -method
 len -funnction
 count - function
----------------------------------------------------------------
"""
print(len(ls))
print(len(tp))

print(ls.count('css'))
print(tp.count('python'))

search = 10 in my_range
print(search)

