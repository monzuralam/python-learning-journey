fruits = ['apple', 'banana', 'mango', 'orange', 'pineapple', 'cherry']

# sort assending
fruits.sort()
print(fruits)

# sort decending
fruits.sort( reverse = True)
print(fruits)

# customize sort function using key = function
new_num = [200, 150, 100, 88, 40, 55]

def filter_num(n):
    return abs(n - 50)

new_num.sort(key = filter_num)
print(new_num)

# sort function case sensitive
new_list = ['book', 'Pen', 'cookie', 'Notepad', 'Pencil']
new_list.sort()
print('default sort:')
print(new_list)

# fix with key = str.lower
new_list.sort( key = str.lower )
print(new_list)

# Reverse order
new_list.reverse()
print(new_list)