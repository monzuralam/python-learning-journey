foods = ('Rice', 'Biriyani', 'Polao', 'Beaf', 'Mutton')

salad = ('Cucumber', 'Radis')

# len
print(len(foods))

# add item
b = list(foods)
b.append('Chicken')
b = tuple(b)
print(b)

c = b + salad
print(c)

# delete
c = list(c)
c.remove('Mutton')
c = tuple(c)
print(c)

# unpack tupples
(rice, *other) = foods
print(rice)
print(other)