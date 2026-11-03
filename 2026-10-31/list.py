# List
fruits = ['Apple', 'Banana', 'Cherry', 'Mango', 'Jackfruits']

# print 
print(fruits)

# length
print( len(fruits) )

mix_item = ['apple', 'rice', 10, True]
print(type(mix_item))
print(mix_item)

# list create by list constructor
new_item = list(('apple', 'banana', 'cherry', 'mango'))
print(new_item)

# change item value
new_item[1] = 'luche'
print(new_item)

# change range item value
new_item[2:3] = ['kiwi', 'peer']
print(new_item)

# insert items
new_item.insert(2, 'rice')
print(new_item)

# append items
new_item.append('nexa')
print(new_item)

# extend to add any iterable objects( list, dict, tuple, sets etc )
new_fruits = ['papaya', 'pineapple']
new_item.extend(new_fruits)
snacks_item = ('halim', 'ruti')
new_item.extend(snacks_item)
print(new_item)

# remove item
new_item.remove('ruti')
print(new_item)

# remove item by index
new_item.pop(1)
print(new_item)

# del index completely
del new_item[1]
print(new_item)

# clear list
new_item.clear()
print(new_item)

# loop the list
current_list = ['apple', 'banana', 'cherry'] 
for x in current_list:
    print(x)

# loop through the index number
for i in range(len(current_list)):
    print(i)

# loop through while list
i = 0
while i < len( current_list ):
    print(current_list[i])
    i = i+1

print('='*20)

# shorthand for loop
[print(x) for x in current_list ]