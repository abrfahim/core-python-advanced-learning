
import  os
# delete file
path = './text3.txt'
if os.path.exists(path):
    os.remove(path)

# another way
if os.path.isfile(path):
    os.remove(path)

# delete folder
target = './A'

#empty directory
if os.path.exists(target):
    os.removedirs(target)
    print('Removed')
else:print('No folder found')

# non-empty directory
import  shutil
if os.path.isdir(target):
    shutil.rmtree(target)
    print('Non-empty directory Removed successfully')
else:print('No directory found')