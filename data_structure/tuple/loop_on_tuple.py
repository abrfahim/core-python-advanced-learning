sports = ("football", "cricket", "badminton", "hockey", "hadudu")

# for loop
for play in sports:
    print(play)

print('----------------------------------------------------------------')

for i in range(0, len(sports)):
    print(sports[i])
print('----------------------------------------------------------------')

# while loop
i=0
print(len(sports))
while i<len(sports):
    print("while:", sports[i])
    i=i+1