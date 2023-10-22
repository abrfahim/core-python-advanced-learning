
# Read file
file = open('text1.txt', 'r')

print(file.read())
print('----------------------------------------------------------------')
print(file.readline())      # Read line by line

# all lines
all = file.readlines()
print(all)
print('----------------------------------------------------------------')

# using loop
while True:
    line = file.readline()
    if not line: break
    else: print(line)

# close file - better to use this method
file.close()

# better way to open file; no need to call close; it will automatically handle

with open('text1.txt', 'r') as newfile:
    print(newfile.read())