# File Write
with open('file_write.txt', 'a') as f:
    f.write('Hello, file right world!')

with open('file_write.txt', 'r', encoding='utf-8') as f2:
    print(f2.read())

# existing file overwrite
with open('file_write.txt', 'w') as f3:
    f3.write('Hello, file overwrite world')

# read the latest file content
with open('file_write.txt', 'r') as f4:
    print(f4.read())

# create new file
f5 = open('new_file.txt', 'x')