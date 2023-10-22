# What does file IO do?
# Input/Output operations such as open, close, read, write and append,
# all of which deal with standard disk or tape files.

import os
# os.listdir method

path = '../file_io'
all_files = os.listdir(path)

print(all_files)    #show all files and directories

# check file or not
for file in all_files:
    if os.path.isfile(os.path.join(path, file)):
        print("{} is a file".format(file))

print('----------------------------------------------------------------')

# os.scandir() method
allFiles = os.scandir(path)
for i in allFiles:
    if (i.is_file()):
        print("{} is a file".format(i.name))

print('----------------------------------------------------------------')

# pathlib module
import pathlib
path_obj = pathlib.Path(path)

for file in path_obj.iterdir():
    if file.is_file():
        print("{} is a file".format(file.name))