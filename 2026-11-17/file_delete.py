import os

# delete file & print
if os.remove('file_delete.txt'):
    print("file delete successfully!!!")
else:
    print("oops!!!")

# before delete file check file exits
if os.path.exists('file_delete.txt'):
    os.remove('file_delete.txt')
else:
    print('operation failed')

# delete folder/directory
os.rmdir('sample')