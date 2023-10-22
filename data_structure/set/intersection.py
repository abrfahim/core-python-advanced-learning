
set1 = {1,23,24,25,26,27,28,29,30,31}
set2 = {1,23,5,6,23,54,27}

intersection  = set1 & set2
print(intersection)

union = set1 | set2
print(union)

difference = set1 - set2
print(difference)

# remove common elements
rce = set1 ^ set2
print(rce)