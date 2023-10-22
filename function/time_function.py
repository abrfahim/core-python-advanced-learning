# In Python, the time() function returns the number of seconds passed since epoch (the point where time begins)

import time
import datetime

print(time.time())
a = 1697605023.5955954
print(time.ctime(a))
print('--------------------------------------------------------')

# sleep timer
print("Hello I am starting")
#time.sleep(2)
print("Hello I am ending")
print('--------------------------------------------------------')

#localtime
print(time.localtime(a))
print('--------------------------------------------------------')

# current datatime
print(datetime.datetime.now())
print('--------------------------------------------------------')

# utc time
x = datetime.datetime.utcnow()
print(x)
print('--------------------------------------------------------')

# get today
y = datetime.date.today()
print(y)
print('--------------------------------------------------------')

#timestamp
z = datetime.date.fromtimestamp(1234567890)
print(z)
print(z.year)
print(z.month)
print(z.day)