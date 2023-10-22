
name= 'Md. Anis Chowdhury'
txt ="Welcome to the journey of PHP Dvelopment. PHP is day by day turning into a dead language"
#uppercase
upper = name.upper()
print(upper)
print("--------------------------------")

#lowercase
lower = name.lower()
print(lower)
print("--------------------------------")

# replace - (old values; new values; count- how many times to replace)

newTxt = txt.replace("PHP", "Python")
modtxt = txt.replace("PHP", "Python",1)
print(newTxt)
print(modtxt)
print("--------------------------------")

#split - The split() method splits a string into a list.

list = 'Mango, Apple, Banana,BlackBerry'
list1 = list.split(',')             # , is separator
print(list1)

car = "Audi Python JavaScript Java Tesla Suzuki"
car1 = car.split(' ')
print(car1)
print("--------------------------------")

#slice - The slice() method
obj ="Abrar Fahim"
obj1 = obj[0:5:1]               # slicing - start:end:step
print(obj1)

abc = "R A H I M"
output= abc[0::2]
print(output)
print("--------------------------------")

#concating
recog = "Mr."
txt="Welcome to our website"
fname = "Sonet"
lname = "Chowdhury"

showText = txt + " " + recog + fname +" "+ lname
print(showText)