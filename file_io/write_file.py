
# overwrite - existing files document will be overwritten and new files will be written
with open('text3.txt', 'w') as overwrite_file:
    overwrite_file.write('This is our new line')


# append - add some new line
with open('text2.txt','a') as append_file:
    append_file.write("--------------------------Tree is the best friend")


# create nex file
with open('newfile.txt', 'w') as newfile:
    newfile.write("I am new file")