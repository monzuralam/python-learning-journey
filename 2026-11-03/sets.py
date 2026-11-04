# Set is unordered, unchangable, unindex collection
items = {'apple', 'banana', 'cherry'}

print(items) # print set

print(len(items)) # set lenght

# We can set by the set constructor also
new_food = set(('rice', 'fish', 'meat', 'patato', 'biriyani', 'halim'))
print(new_food) #print

print('='*20)

# access set item
for x in items:
    print(x)

print('='*20)

print('apple' in items)

print('banana' not in items)

# Add value
items.add('guava')
print(items)

items.update(new_food)
print(items)

# you can add any kind of iterable items also
items.update(('lentils', 'salad'))
print(items)

"""
remove items
- remove 
- discard
- pop
"""
items.remove('lentils')
print(items)

items.discard('rice')
print(items)

items.pop() # last item remove
print(items)

# clear set
items.clear()
print(items)

# del set
# del items
# print(items)
print('='*20)

"""
loop set
"""
for x in new_food:
    print(x)

print('='*20)

"""
join
- union & update
- intersection
- difference
- symetric_difference
"""
# union
set1 = {"rice", "meat", "fish", "water"}
set2 = {20, 100, 80, 15}

print(set1)
print(set2)
print('='*20)

print(set1.union(set2))

# you can union multiple item by comma
print(set1.union(set2, new_food))

# you can use | insted of union method
print(set1 | set2) 

# you can union tuple on the set
new_tuple = ('Blackseed', 'Nut')
print(set1.union(new_tuple))

# update: its modify the main set 
set1.update({'Fucka', 'Chotpoti'})
print(set1)

# intersection
print(set1.intersection(new_food))

# intersection can be done by & 
print(set1 & {'water', 'fish'})

# difference
print(set1.difference({'rice', 'water', 'fish'}))

# difference can be show - operator
print(set1 - {'rice', 'water', 'fish'} )

# symantic difference
print(set1.symmetric_difference({'rice', 'water', 'fish'}))

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# symmetric difference can by ^ also
set3 = set1 ^ set2
print(set3)
print('='*20)

"""
# Frozen set
"""
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))