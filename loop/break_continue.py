# The break statement is used to terminate the loop immediately when it is encountered.
# Continue: The continue statement in Python is used to
# skip the remaining code inside a loop for the current iteration only.


for i in range(1,11):
    if i==5:
        break
    print("After Break:",i)

for i in range(1,11):
    if i>=5 and i<=8:
        continue
    print("After Continue:", i)
print("----------------------------------------------------------------")
# while loop
i =1
while i<=10:
    if i==5:
        break
    print("After Break:",i)
    i = i + 1

k =0
while k<=10:
    if (k>5 and k<=8):
        k = k + 1
        continue
    print("After Continue:", k)
    k = k + 1

