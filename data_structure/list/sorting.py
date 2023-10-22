
numbers=[1,3,4,56,9,52,31,12,21,24,58]
# sort method modify orginal list
numbers.sort()  #ascending order
print("Ascending order:", numbers)
numbers.sort(reverse=True)  #descending order
print("descending order:", numbers)

#sorted method didn't modify orginal list and just return a new list

num =[1,2,4,7,3,56,32,19]
a = sorted(num)
b = sorted(num,reverse=True)
print("sorted and return a new list >>>ascending order:",a)
print("sorted and return a new list >>>descending order:",b)

print("original list", num)
