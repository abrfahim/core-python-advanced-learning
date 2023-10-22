
# return a list of 1 to 30
num=[]
for i in range(1,31):
    num.append(i)
num.sort(reverse=True)
print(num)

#shortend - list comprehension
a =[i for i in range(1,31)]         # i single for appending; refer stroing
a.sort(reverse=True)
print("a list return:", a)