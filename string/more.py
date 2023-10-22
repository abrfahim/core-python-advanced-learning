# format method:

#The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.

fname = 'Sonet'
lname= 'Chowdhury'
txt= 'Welcome to our website'
recog= 'Mr.'

# here 4 set braces store 4 variables value, so more variables need more braces
output = "{} {} {} {}".format(txt,recog,fname, lname)
print(output)

output1 = "The dynamic way: {txt} {recog} {fname} {lname}".format(txt=txt,recog=recog,fname=fname, lname=lname)
print(output1)

# escape characters - To insert characters that are illegal in a string,
# use an escape character. An escape character is a backslash \ followed by the character you want to insert.

words = "Teacher said that, \"Tanim is a good boy\""
print(words)