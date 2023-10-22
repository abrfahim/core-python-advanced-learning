# Logical operators are used to combine conditional statements:
#
# Operator	                        Description	                                             Example
# and 	                Returns True if both statements are true	                    x < 5 and  x < 10
# or	            Returns True if one of the statements is true	                    x < 5 or x < 4
# not	            Reverse the result, returns False if the result is true	            not(x < 5 and x < 10)


num1 = 10
num2 = 50

print(num1<num2 and num1>num2)
print(num1==num2 or num1!=num2)
print(num1==num2 and num1!=num2)
print(not(num1==num2 and num1!=num2))