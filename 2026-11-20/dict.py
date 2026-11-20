a = {'name':'shakil', 'age':'18', 'city': 'rangpur'}
b = dict(name = 'BMW', price = '200k', model = '2022', color = 'black' )

print(type(a))
print(len(a))

# access item
print(b.get('name'))
print(b.values())
print(b.items())

# update item
b.update({'color':'white'})
print(b)

# add item
b.update({'condition': 'good'})
print(b)

# remove item
b.pop('condition')
print(b)

b.popitem()
print(b)

# copy item
c = b.copy()
print(c)

d = dict(c)
print(d)